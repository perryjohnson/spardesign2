"""Write initial TrueGrid files for one Sandia blade station.

Usage
-----
start an IPython (qt)console with the pylab flag:
$ ipython qtconsole --pylab
or
$ ipython --pylab
Then, from the prompt, run this script:
|> %run create_stnXX_mesh

Author: Perry Roth-Johnson
Last updated: March 15, 2014

"""


import matplotlib.pyplot as plt
import lib.blade as bl
reload(bl)
import lib.poly_utils as pu
reload(pu)
from shapely.geometry import Polygon


# SET THESE PARAMETERS -----------------
station_num = 8
# --------------------------------------
plt.close('all')

# load the Sandia blade
m = bl.MonoplaneBlade('Sandia blade SNL100-00', 'sandia_blade',
    rotate_airfoil_coords=False)

# pre-process the station dimensions
station = m.list_of_stations[station_num-1]
station.airfoil.create_polygon()
station.structure.create_all_layers()
station.structure.save_all_layer_edges()
station.structure.write_all_part_polygons()

# plot the parts
station.plot_parts(alternate_layers=False)

# access the structure for this station
st = station.structure

# upper spar cap -----------------------------------------------------------
label = 'upper spar cap'

# create the bounding polygon
points_usc = [
    (-0.75, 2.51653955),
    (-0.74, 2.50903949),
    ( 0.74, 2.51551666),
    ( 0.75, 2.52331886),
    ( 0.75, 3.0),
    (-0.75, 3.0)
    ]
bounding_polygon = Polygon(points_usc)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'triax', label, 
    bounding_polygon)

# lower spar cap -----------------------------------------------------------
label = 'lower spar cap'

# create the bounding polygon
points_lsc = [
    (-0.75,-points_usc[0][1]),
    (-0.74,-points_usc[1][1]),
    ( 0.74,-points_usc[2][1]),
    ( 0.75,-points_usc[3][1]),
    ( 0.75,-3.0),
    (-0.75,-3.0)
    ]
bounding_polygon = Polygon(points_lsc)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'triax', label, 
    bounding_polygon)

# TE reinforcement ---------------------------------------------------------
label = 'TE reinforcement'

# create the bounding polygon
points_te = [
    (1.91712200,   1.94726517),
    (2.0, 2.04),
    (3.0, 2.0),
    (3.0,-2.0),
    (2.0,-2.04),
    (1.91712200,  -1.94726517)
    ]
bounding_polygon = Polygon(points_te)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)

# LE panel -----------------------------------------------------------------
label = 'LE panel'

# create the bounding polygon
points_le = [
    (-3.00,-3.0),
    (-0.836,-3.0),
    (-0.836, -2.49145691),
    (-0.846, -2.47812368),
    (-1.5, 0.0),
    (-0.846,  2.47812368),
    (-0.836,  2.49145691),
    (-0.836, 3.0),
    (-3.00, 3.0)
    ]
bounding_polygon = Polygon(points_le)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_1, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_1, 'triax', label, 
    bounding_polygon)

# upper aft panel 1 -------------------------------------------------------
label = 'upper aft panel 1'
# create the bounding polygon
points_ur = [
    (0.836, 2.8),
    (2.0,  2.8),
    points_te[1],
    points_te[0],
    (1.91712200,   1.9),
    (1.2, 2.0),
    (0.846,   2.48490299),
    (0.836,   2.49823622)
    ]
bounding_polygon = Polygon(points_ur)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)

# lower aft panel 1 -------------------------------------------------------
label = 'lower aft panel 1'
# create the bounding polygon
points_lr = [
    (0.836, -2.8),
    (2.0,  -2.8),
    points_te[-2],
    points_te[-1],
    (points_ur[-4][0],   -points_ur[-4][1]),
    (1.2, -2.0),
    (0.846,   -points_ur[-2][1]),
    (0.836,   -points_ur[-1][1])
    ]
bounding_polygon = Polygon(points_lr)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)

# above shear web 1 ----------------------------------------------------------
label = 'above shear web 1'

# create the bounding polygon
points_asw1 = [
    (-0.75, 2.7),
    (-0.75, 2.4),
    (-0.836, 2.4),
    (-0.836, 2.7)
    ]
bounding_polygon = Polygon(points_asw1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# below shear web 1 ----------------------------------------------------------
label = 'below shear web 1'

# create the bounding polygon
points_bsw1 = [
    (-0.75, -2.7),
    (-0.75, -2.4),
    (-0.836, -2.4),
    (-0.836, -2.7)
    ]
bounding_polygon = Polygon(points_bsw1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# above shear web 2 ----------------------------------------------------------
label = 'above shear web 2'

# create the bounding polygon
points_asw2 = [
    (0.75, 2.7),
    (0.75, 2.4),
    (0.836, 2.4),
    (0.836, 2.7)
    ]
bounding_polygon = Polygon(points_asw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# below shear web 2 ----------------------------------------------------------
label = 'below shear web 2'

# create the bounding polygon
points_bsw2 = [
    (0.75, -2.7),
    (0.75, -2.4),
    (0.836, -2.4),
    (0.836, -2.7)
    ]
bounding_polygon = Polygon(points_bsw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# left of shear web 1 -------------------------------------------------------
label = 'left of shear web 1'

# create the bounding polygon
points_lsw1 = points_le[2:-2]
bounding_polygon = Polygon(points_lsw1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_1, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_1, 'triax', label, 
    bounding_polygon)

# right of shear web 1 -------------------------------------------------------
label = 'right of shear web 1'

# create the bounding polygon
points_rsw1 = [
    points_usc[0],
    points_usc[1],
    (0.0, 0.0),
    points_lsc[1],
    points_lsc[0]
    ]
bounding_polygon = Polygon(points_rsw1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'triax', label, 
    bounding_polygon)

# left of shear web 2 -------------------------------------------------------
label = 'left of shear web 2'

# create the bounding polygon
points_lsw2 = [
    points_usc[3],
    points_usc[2],
    (0.0, 0.0),
    points_lsc[2],
    points_lsc[3]
    ]
bounding_polygon = Polygon(points_lsw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'triax', label, 
    bounding_polygon)

# right of shear web 2 -------------------------------------------------------
label = 'right of shear web 2'

# create the bounding polygon
points_rsw2 = [
    points_ur[-1],
    points_ur[-2],
    (1.5, 0.0),
    points_lr[-2],
    points_lr[-1]
    ]
bounding_polygon = Polygon(points_rsw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)




# show the plot
plt.show()

# write the TrueGrid input file for mesh generation ---------------------
st.write_truegrid_inputfile(
    interrupt_flag=True, 
    additional_layers=[
        st.spar_cap.layer['upper'],
        st.spar_cap.layer['lower'],
        st.TE_reinforcement.layer['uniax'],
        st.aft_panel_1.layer['upper'],
        st.aft_panel_1.layer['lower'],
        st.LE_panel.layer['foam'],
        st.shear_web_1.layer['biax, left'],
        st.shear_web_1.layer['foam'],
        st.shear_web_1.layer['biax, right'],
        st.shear_web_2.layer['biax, left'],
        st.shear_web_2.layer['foam'],
        st.shear_web_2.layer['biax, right']
    ])