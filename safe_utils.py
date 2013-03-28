"""
A module to translate data from a 2D cross-section grid file (from TrueGrid)
into a SAFE input file.

Author: Perry Roth-Johnson
Last updated: March 28, 2013

"""


import numpy as np
import abaqus_utils as au


class SafeInputFile:
    """
The SafeInputFile class contains methods for translating data from a 2D
cross-section grid file (from TrueGrid) into a SAFE input file.

Usage:
import safe_utils as su
f = su.SafeInputFile(title='square 4x6 cross-section',
safe_filename='cs_safe.txt',
grid_filename='cs_abq.txt',
debug_flag=True)

    """


    def __init__(self, title, safe_filename, grid_filename, debug_flag=False):
        self.title = title
        self.safe_filename = safe_filename
        self.grid_filename = grid_filename
        self.grid = au.AbaqusGrid(grid_filename)
        self._write_input_file(debug_flag=debug_flag)


    def _write_title(self):
        self.safe_file.write(self.title.upper() + '\n')


    def _write_comments(self):
        # write the separator (first line)
        self.safe_file.write('COMMENTS           1' + '\n')
        # write up to 5 lines of comments
        self.safe_file.write('    Material 1 is foam\n')
        self.safe_file.write('END COMMENTS' + '\n')


    def _write_corner_nodes(self):
        # write the separator (first line)
        self.safe_file.write('CORNER NODES' + 3*' ' + '{0:>5d}'.format(self.grid.number_of_corner_nodes) + '\n')
        fmt = '{0:>5d}' + 5*' ' + '{1:> 10.5f}' + '{2:> 10.5f}\n'
        for node in self.grid.node_array:
            if node['is_corner_node'] == 1:
                self.safe_file.write(fmt.format(node['node_no'], node['x2'], node['x3']))


    def _write_midside_nodes(self):
        # write the separator (first line)
        self.safe_file.write('MID-SIDE NODES' + ' ' + '{0:>5d}'.format(self.grid.number_of_midside_nodes) + '\n')
        fmt = '{0:>5d}' + '{1:>5d}' + '{2:> 10.5f}' + '{3:> 10.5f}\n'
        for node in self.grid.node_array:
            if node['is_corner_node'] == 0:
                self.safe_file.write(fmt.format(
                                        node['node_no'], node['node_no'],
                                        node['x2'], node['x3']))


    def _write_materials(self):
        # write the separator (first line)
        self.grid.number_of_materials = 1  # HARDCODED! CHANGE LATER!
        self.safe_file.write('MATERIALS' + 6*' ' + '{0:>5}'.format(self.grid.number_of_materials) + '\n')
        isotropic_fmt = '{0:>5d}{1:>5}{2:>10.3e}{3:>10.3e}{4:>10.2f}{5:>10.2f}\n'
        # write material properties  # HARDCODED FOR FOAM! CHANGE LATER!
        material_no = 1
        itype = 'I'  # isotropic material
        rho = 2.00000e+02  # density = 200 kg/m^3
        E = 2.56000e+08  # Young's modulus = 0.256 GPa
        nu = 3.00000e-01  # Poisson's ratio = 0.3
        alpha = 0.0  # thermal coefficient
        self.safe_file.write(isotropic_fmt.format(material_no,
                                                  itype,
                                                  rho,
                                                  E,
                                                  nu,
                                                  alpha))
        # self.safe_file.write("    1    I        1.     0.256       0.3       0.0\n")


    def _write_elements(self):
        # write the separator (first line)
        self.safe_file.write('ELEMENTS' + 7*' ' + '{0:>5d}'.format(self.grid.number_of_elements) + '\n')
        fmt = '{0:>5d}' + '{1:>5d}' + '{2:>5d}' + '{3:>5d}' + '{4:>5d}' + '{5:>5d}' + '\n'
        for element in self.grid.element_array:
            self.safe_file.write(fmt.format(element['elem_no'],
                                            element['node1'],
                                            element['node2'],
                                            element['node3'],
                                            element['node4'],
                                            element['layer_no'])) # change this to material number later...


    def _write_end_fe_model(self):
        # write the separator (first line)
        self.safe_file.write('END FE MODEL\n')


    def _write_footer(self):
        self.safe_file.write("""LENGTH          60.0
RESTRAINT          1
  102         1    1    1 
EBTFLEX                                                            
       0.0       1.0       1.0       0.0
       0.0       0.0       0.0       0.0
            """)


    def _write_input_file(self, debug_flag=False):
        """
Writes the SAFE input file.

This non-public method is automatically run when a new SafeInputFile instance
is created.

        """

        if debug_flag:
            print 'SAFE input file: ' + self.safe_filename
        # open the input file
        self.safe_file = open(self.safe_filename, 'w+')
        # write to the input file
        self._write_title()
        self._write_comments()
        self._write_corner_nodes()
        # self._write_midside_nodes()
        self._write_materials()
        self._write_elements()
        self._write_end_fe_model()
        self._write_footer()
        # close the input file
        self.safe_file.close()