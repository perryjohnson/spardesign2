spardesign2 (airfoilgrid)
=========================

Takes a wind turbine blade cross-section, creates a 2D mesh with TrueGrid, and
calculates its cross-sectional properties (mass and stiffness matrices) with VABS.

## example
In this example, we use blade station 26 of the Sandia SNL100-00 blade, which
uses a NACA 64-618 airfoil.

1. Open an IPython (pylab) prompt and type:  
`|> %run airfoil_script`  
Several 2D curves will be written to a file named `segments.tg`.
2. Manually copy the contents of this file into the relevant section in
`airfoil.tg` (lines 57-234).
3. Run TrueGrid, and open `airfoil.tg`. The grid will briefly display on the
screen, and then TrueGrid will write the grid to a file called
`stn26.abq` and immediately exit.
4. In the IPython prompt, write input files for VABS and SAFE by typing:  
`|> %run grid_script`
5. In a Windows command prompt, run the VABS input file by typing:  
`> VABSIII stn26.vabs`
6. View the cross-sectional properties calculated by VABS in `stn26.vabs.K`  
Look for the header: **Classical Stiffness Matrix**
7. In a Windows command prompt, run the SAFE input file by typing:  
`> rsvam`  
then type in the Input Filename `stn26.safe`.  
Follow the prompts. Answer 'n' to all questions, except answer 'y' to  
**DO TIMOSHENKO SHEAR CORRECTION FACTORS?**
8. View the cross-sectional properties calculated by SAFE in `stn26.OUT`.  
Look for the header: **STIFFNESS COEFFICIENTS Kappa_I**
9. In an IPython prompt, compare the stiffness matrices calculated by VABS and
SAFE by typing:  
`|> import stiffness_utils as stu`  
`|> stu.compare_vabs_and_safe('stn26.vabs.K','stn26.OUT')`