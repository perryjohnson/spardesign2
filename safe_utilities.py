"""
A module to translate data from a 2D cross-section grid file (from TrueGrid)
into a SAFE input file.

Author: Perry Roth-Johnson
Last updated: February 22, 2013

"""


import numpy as np
import abaqus_utilities as au


class SafeInputFile:
    """
The SafeInputFile class contains methods for translating data from a 2D
cross-section grid file (from TrueGrid) into a SAFE input file.

Usage:
import safe_utilities as su
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


    # def _write_comments(self):
    #     # write the separator (first line)
    #     self.safe_file.write('COMMENTS' + '\n')
    #     self.safe_file.write('END COMMENTS' + '\n')


    # corner nodes
    def _write_nodes(self):
        # write the separator (first line)
        self.safe_file.write('CORNER NODES' + 3*' ' + '{0:>5}'.format(self.grid.number_of_nodes) + '\n')
        fmt = '{0:>5}' + 5*' ' + '{1:>10}' + '{2:>10}\n'
        for node in self.grid.node_array:
            self.safe_file.write(fmt.format(node['node_no'], node['x2'], node['x3']))


    # mid-side nodes


    def _write_materials(self):
        # write the separator (first line)
        self.safe_file.write('MATERIALS' + 6*' ' + '{0:>5}'.format(self.grid.number_of_materials) + '\n')
        # write material properties


    def _write_elements(self):
        # write the separator (first line)
        self.safe_file.write('ELEMENTS' + 7*' ' + '{0:>5}'.format(self.grid.number_of_elements) + '\n')
        fmt = '{0:>5}' + '{1:>5}' + '{2:>5}' + '{3:>5}' + '{4:>5}' + '{5:>5}' + '\n'
        for element in self.grid.element_array:
            self.safe_file.write(fmt.format(element['elem_no'],
                                            element['node1'],
                                            element['node2'],
                                            element['node3'],
                                            element['node4'],
                                            element['layer_no']))  # change this to material number later...


    def _write_end_fe_model(self):
        # write the separator (first line)
        self.safe_file.write('END FE MODEL\n')


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
        # self._write_comments()
        self._write_nodes()
        # self._write_midside_nodes()
        # self._write_materials()
        self._write_elements()
        self._write_end_fe_model()
        # close the input file
        self.safe_file.close()