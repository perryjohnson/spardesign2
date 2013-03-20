spardesign2 (airfoilgrid)
=========================

Python modules and TrueGrid batch scripts to create a 2D cross-sectional mesh
for blade station 26 in the Sandia SNL100-00 blade. This station uses the
NACA 64-618 airfoil.  

1. Open an IPython (pylab) prompt and type:  
```
|> %run airfoil_curves
```
2. Several 2D curves will be written to a file named `segments.tg`. Manually
copy the contents of this file into the relevant section in `airfoil.tg`
(lines 54-237).
3. Run TrueGrid, open `airfoil.tg`, and view the grid on the screen.