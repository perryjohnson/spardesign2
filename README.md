spardesign2 (airfoilgrid)
=========================

Takes a wind turbine blade cross-section, creates a 2D mesh with TrueGrid, and calculates its cross-sectional properties (mass and stiffness matrices) with VABS.

##example
In this example, we use blade station 26 of the Sandia SNL100-00 blade, which uses a NACA 64-618 airfoil.

1. Open an IPython (pylab) prompt and type:  
`|> %run airfoil_curves`
2. Several 2D curves will be written to a file named `segments.tg`. Manually
copy the contents of this file into the relevant section in `airfoil.tg`
(lines 57-234).
3. Run TrueGrid, and open `airfoil.tg`. The grid will briefly display on the screen, and then TrueGrid will write the grid to a file `blade_station_25_abq.txt` and immediately exit.
4. In the IPython prompt, write a VABS input file by typing:  
`|> import vabs_utils as vu`  
`|> f = vu.VabsInputFile('blade_station_26_vabs.dat','blade_station_26_abq.txt')`
5. In a Windows command prompt, run the VABS input file by typing:  
`> VABSIII blade_station_26_vabs.dat`
6. View the cross-sectional properties in `blade_station_26_vabs.dat.K`