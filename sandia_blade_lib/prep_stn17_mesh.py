"""Write initial TrueGrid files for one Sandia blade station.

Usage
-----
start an IPython (qt)console with the pylab flag:
$ ipython qtconsole --pylab
or
$ ipython --pylab
Then, from the prompt, run this script:
|> %run sandia_blade_lib/prep_stnXX_mesh.py
or
|> import sandia_blade_lib/prep_stnXX_mesh

Author: Perry Roth-Johnson
Last updated: April 10, 2014

"""


import matplotlib.pyplot as plt
import lib.blade as bl
import lib.poly_utils as pu
from shapely.geometry import Polygon


# SET THESE PARAMETERS -----------------
station_num = 17
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
station.plot_parts()

# access the structure for this station
st = station.structure

# upper spar cap -----------------------------------------------------------
label = 'upper spar cap'

# create the bounding polygon
usc = st.spar_cap.layer['upper']
is2 = st.internal_surface_2.layer['resin']
points_usc = [
    (-0.75, usc.left[0][1]),              # SparCap_upper.txt
    is2.polygon.interiors[0].coords[-2],  # InternalSurface2_resin.txt
    ( 0.74, 1.03530366),                  # InternalSurface2_resin.txt
    ( 0.75, usc.right[1][1]),             # SparCap_upper.txt
    ( 0.75, 1.8),
    (-0.75, 1.8)
    ]
bounding_polygon = Polygon(points_usc)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
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
lsc = st.spar_cap.layer['lower']
points_lsc = [
    (-0.75,-1.9),
    ( 0.75,-1.9),
    ( 0.75000000,  lsc.right[0][1]),      # SparCap_lower.txt
    (0.74000000,  -1.06550534),          # InternalSurface2_resin.txt
    is2.polygon.interiors[0].coords[-1],  # InternalSurface2_resin.txt
    (-0.75000000,  lsc.left[1][1])        # SparCap_lower.txt
    ]
bounding_polygon = Polygon(points_lsc)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_2, 'triax', label, 
    bounding_polygon)

# TE reinforcement, upper 1 ------------------------------------------------
label = 'TE reinforcement, upper 1'

# create the bounding polygon
ter = st.TE_reinforcement.layer['foam']
points_teu1 = [
    (ter.top[0][0], 0.35),              # TE_Reinforcement_foam.txt
    tuple(ter.top[0]),                  # TE_Reinforcement_foam.txt
    (3.71, 0.18),
    (3.91964530,   0.12466663),         # InternalSurface4_resin.txt
    (3.91964530,   0.35)                # InternalSurface4_resin.txt
    ]
bounding_polygon = Polygon(points_teu1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'foam', label,
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, lower 1 ------------------------------------------------
label = 'TE reinforcement, lower 1'

# create the bounding polygon
points_tel1 = [
    (ter.bottom[0][0], -0.1),              # TE_Reinforcement_foam.txt
    tuple(ter.bottom[1]),                  # TE_Reinforcement_foam.txt
    (3.71, 0.09),
    (3.8, 0.12),
    (3.91964530,   0.12466663),         # InternalSurface4_resin.txt
    (3.91964530,   -0.1)                # InternalSurface4_resin.txt
    ]
bounding_polygon = Polygon(points_tel1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'foam', label,
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, upper 2 ------------------------------------------------
label = 'TE reinforcement, upper 2'

# create the bounding polygon
points_teu2 = [
    points_teu1[-1],
    points_teu1[-2],
    (3.96697377,   0.12058056),    # InternalSurface4_triax.txt
    (3.96697377,   0.35) # InternalSurface4_triax.txt
    ]
bounding_polygon = Polygon(points_teu2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'foam', label,
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, lower 2 ------------------------------------------------
label = 'TE reinforcement, lower 2'

# create the bounding polygon
points_tel2 = [
    (points_teu2[0][0], -0.1),
    points_teu2[1],
    points_teu2[2],
    (points_teu2[2][0], -0.1)
    ]
bounding_polygon = Polygon(points_tel2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'foam', label,
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, upper 3 ------------------------------------------------
label = 'TE reinforcement, upper 3'

# create the bounding polygon
points_teu3 = [
    points_teu2[-1],
    points_teu2[-2],
    ter.polygon.exterior.coords[0],    # TE_Reinforcement_foam.txt
    (ter.polygon.exterior.coords[0][0], 0.35) # TE_Reinforcement_foam.txt
    ]
bounding_polygon = Polygon(points_teu3)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'foam', label,
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, lower 3 ------------------------------------------------
label = 'TE reinforcement, lower 3'

# create the bounding polygon
points_tel3 = [
    (points_teu3[0][0], -0.1),
    points_teu3[1],
    points_teu3[2],
    (points_teu3[2][0], -0.1)
    ]
bounding_polygon = Polygon(points_tel3)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'foam', label,
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, upper 4 ------------------------------------------------
label = 'TE reinforcement, upper 4'

# create the bounding polygon
es = st.external_surface.layer['gelcoat']
points_teu4 = [
    points_teu3[-1],
    points_teu3[-2],
    (4.71227000,   0.005),  # TE_Reinforcement_uniax.txt
    (4.71227000,   0.02052196),  # TE_Reinforcement_uniax.txt
    es.polygon.exterior.coords[-2],
    (4.71227000,   0.35) # TE_Reinforcement_uniax.txt
    ]
bounding_polygon = Polygon(points_teu4)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# TE reinforcement, lower 4 ------------------------------------------------
label = 'TE reinforcement, lower 4'

# create the bounding polygon
points_tel4 = [
    (points_teu4[0][0], -0.1),
    points_teu4[1],
    points_teu4[2],
    (4.71227000,  -0.01761200),   # TE_Reinforcement_uniax.txt
    es.polygon.exterior.coords[-1],
    (points_teu4[2][0], -0.1)
    ]
bounding_polygon = Polygon(points_tel4)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.TE_reinforcement, 'uniax', label, 
    bounding_polygon)

# LE panel -----------------------------------------------------------------
label = 'LE panel'

# create the bounding polygon
lep = st.LE_panel.layer['foam']
is1 = st.internal_surface_1.layer['resin']
points_le = [
    (-3.00,-2.0),
    (-0.836,-2.0),
    tuple(lep.bottom[0]),  # LE_Panel_foam.txt
    is1.polygon.interiors[0].coords[0],  # InternalSurface1_resin.txt
    (-1.5, 0.0),
    is1.polygon.interiors[0].coords[1],  # InternalSurface1_resin.txt
    tuple(lep.top[1]),  # LE_Panel_foam.txt
    (-0.836, 2.0),
    (-3.00, 2.0)
    ]
bounding_polygon = Polygon(points_le)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
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
ap1u = st.aft_panel_1.layer['upper']
is3 = st.internal_surface_3.layer['resin']
points_ap1u = [
    (0.836, 1.8),
    (ap1u.right[1][0], 1.8),              # AftPanel1_upper.txt
    tuple(ap1u.right[1]),                 # AftPanel1_upper.txt
    (2.42654667,   0.65698556),           # InternalSurface3_resin.txt
    (1.2, 0.8),
    is3.polygon.interiors[0].coords[-2],  # InternalSurface3_resin.txt
    tuple(ap1u.left[0])                   # AftPanel1_upper.txt
    ]
bounding_polygon = Polygon(points_ap1u)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
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
ap1l = st.aft_panel_1.layer['lower']
points_ap1l = [
    (0.836, -1.8),
    (ap1l.right[0][0], -1.8),             # AftPanel1_lower.txt
    tuple(ap1l.right[0]),                 # AftPanel1_lower.txt
    (2.42654667,  -0.41348357),           # InternalSurface3_resin.txt
    (1.2, -0.8),
    is3.polygon.interiors[0].coords[-1],  # InternalSurface3_resin.txt
    tuple(ap1l.left[1])                   # AftPanel1_lower.txt
    ]
bounding_polygon = Polygon(points_ap1l)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)

# upper aft panel 2 -------------------------------------------------------
label = 'upper aft panel 2'

# create the bounding polygon
ap2u = st.aft_panel_2.layer['upper']
is4 = st.internal_surface_4.layer['resin']
sw3br = st.shear_web_3.layer['biax, right']
points_ap2u = [
    (sw3br.right[0][0], 1.4),
    (ap2u.right[1][0], 1.4),              # AftPanel2_upper.txt
    tuple(ap2u.right[1]),                 # AftPanel2_upper.txt
    (3.70787000,   0.25303068),           # InternalSurface4_resin.txt
    (3.0, 0.3),
    is4.polygon.interiors[0].coords[-2],  # InternalSurface4_resin.txt
    tuple(ap2u.left[0])                   # AftPanel2_upper.txt
    ]
bounding_polygon = Polygon(points_ap2u)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)

# lower aft panel 2 -------------------------------------------------------
label = 'lower aft panel 2'

# create the bounding polygon
ap2l = st.aft_panel_2.layer['lower']
is4 = st.internal_surface_4.layer['resin']
sw3br = st.shear_web_3.layer['biax, right']
points_ap2l = [
    (sw3br.right[0][0], -1.4),
    (ap2l.right[0][0], -1.4),             # AftPanel2_lower.txt
    tuple(ap2l.right[0]),                 # AftPanel2_lower.txt
    (3.70787000,   0.02559952),           # InternalSurface4_resin.txt
    (3.0, 0.0),
    is4.polygon.interiors[0].coords[-1],  # InternalSurface4_resin.txt
    tuple(ap2l.left[1])                   # AftPanel2_lower.txt
    ]
bounding_polygon = Polygon(points_ap2l)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)

# above shear web 1 ----------------------------------------------------------
label = 'above shear web 1'

# create the bounding polygon
points_asw1 = [
    (-0.75, 2.1),
    (-0.75, 1.0),
    (-0.836, 1.0),
    (-0.836, 2.1)
    ]
bounding_polygon = Polygon(points_asw1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# below shear web 1 ----------------------------------------------------------
label = 'below shear web 1'

# create the bounding polygon
points_bsw1 = [
    (-0.75, -2.1),
    (-0.75, -1.0),
    (-0.836, -1.0),
    (-0.836, -2.1)
    ]
bounding_polygon = Polygon(points_bsw1)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# above shear web 2 ----------------------------------------------------------
label = 'above shear web 2'

# create the bounding polygon
points_asw2 = [
    (0.75, 2.1),
    (0.75, 1.0),
    (0.836, 1.0),
    (0.836, 2.1)
    ]
bounding_polygon = Polygon(points_asw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# below shear web 2 ----------------------------------------------------------
label = 'below shear web 2'

# create the bounding polygon
points_bsw2 = [
    (0.75, -2.1),
    (0.75, -1.0),
    (0.836, -1.0),
    (0.836, -2.1)
    ]
bounding_polygon = Polygon(points_bsw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)


# above shear web 3 ----------------------------------------------------------
label = 'above shear web 3'

# create the bounding polygon
sw3bl = st.shear_web_3.layer['biax, left']
points_asw3 = [
    (sw3bl.left[0][0], 1.0),
    (sw3bl.left[0][0], 0.1),
    (sw3br.right[0][0], 0.1),
    (sw3br.right[0][0], 1.0)
    ]
bounding_polygon = Polygon(points_asw3)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)

# below shear web 3 ----------------------------------------------------------
label = 'below shear web 3'

# create the bounding polygon
points_bsw3 = [
    (sw3bl.left[0][0], -1.0),
    (sw3bl.left[0][0], -0.1),
    (sw3br.right[0][0], -0.1),
    (sw3br.right[0][0], -1.0)
    ]
bounding_polygon = Polygon(points_bsw3)
pu.plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
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
    points_lsc[-2],
    points_lsc[-1]
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
    points_lsc[3],
    points_lsc[2]
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
    points_ap1u[-1],
    points_ap1u[-2],
    (1.5, 0.0),
    points_ap1l[-2],
    points_ap1l[-1]
    ]
bounding_polygon = Polygon(points_rsw2)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)

# left of shear web 3 -------------------------------------------------------
label = 'left of shear web 3'

# create the bounding polygon
points_lsw3 = [
    points_ap1u[2],
    points_ap1u[3],
    (2.0, 0.0),
    points_ap1l[3],
    points_ap1l[2]
    ]
bounding_polygon = Polygon(points_lsw3)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_3, 'triax', label, 
    bounding_polygon)

# right of shear web 3 -------------------------------------------------------
label = 'right of shear web 3'

# create the bounding polygon
points_rsw3 = [
    points_ap2u[-1],
    points_ap2u[-2],
    (3.0, 0.0),
    points_ap2l[-2],
    points_ap2l[-1]
    ]
bounding_polygon = Polygon(points_rsw3)
pu.plot_polygon(bounding_polygon, 'None', '#000000')
# cut the new layer polygons
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'resin', label, 
    bounding_polygon)
pu.cut_plot_and_write_alt_layer(st.internal_surface_4, 'triax', label, 
    bounding_polygon)




# show the plot
plt.show()

# write the TrueGrid input file for mesh generation ---------------------
st.write_truegrid_inputfile(
    interrupt_flag=True, 
    additional_layers=[
        st.spar_cap.layer['upper'],
        st.spar_cap.layer['lower'],
        st.aft_panel_1.layer['upper'],
        st.aft_panel_1.layer['lower'],
        st.aft_panel_2.layer['upper'],
        st.aft_panel_2.layer['lower'],
        st.LE_panel.layer['foam'],
        st.shear_web_1.layer['biax, left'],
        st.shear_web_1.layer['foam'],
        st.shear_web_1.layer['biax, right'],
        st.shear_web_2.layer['biax, left'],
        st.shear_web_2.layer['foam'],
        st.shear_web_2.layer['biax, right'],
        st.shear_web_3.layer['biax, left'],
        st.shear_web_3.layer['foam'],
        st.shear_web_3.layer['biax, right']
    ],
    alt_TE_reinforcement=True,
    soft_warning=False)