"""Write initial TrueGrid files for one Sandia blade station.

Usage
-----
start an IPython (qt)console with the pylab flag:
$ ipython qtconsole --pylab
or
$ ipython --pylab
Then, from the prompt, run this script:
|> %run create_stn01_mesh

Author: Perry Roth-Johnson
Last updated: March 15, 2014

"""

import os
import matplotlib.pyplot as plt
import numpy as np
import lib.blade as bl
reload(bl)
from shapely.geometry import Polygon
from descartes import PolygonPatch
import lib.layer as l

# load the Sandia blade
m = bl.MonoplaneBlade('Sandia blade SNL100-00', 'sandia_blade',
    rotate_airfoil_coords=False)

# pick a station number
station_num = 1

# pre-process the station dimensions
station = m.list_of_stations[station_num-1]
station.airfoil.create_polygon()
station.structure.create_all_layers()
station.structure.save_all_layer_edges()
# station.structure.write_truegrid_inputfile(interrupt_flag=True)
station.structure.write_all_part_polygons()

# plot the parts
station.plot_parts(alternate_layers=False)

# cut up the layer polygons to prepare for grid generation
def cut_polygon(original, bounding):
    """Cut the original layer polygon with the bounding polygon."""
    return original.intersection(bounding)

def plot_polygon(p, face_color, edge_color='r'):
    """Plot a polygon on the current axes."""
    # get the current axes, so we can add polygons to the plot
    ax = plt.gca()
    patch = PolygonPatch(p, fc=face_color, ec=edge_color, alpha=0.8)
    ax.add_patch(patch)

def cut_plot_and_write_alt_layer(part, material, ext_label, b_polygon):
    """Cut, plot, and write a polygon for an alternate layer."""
    l = part.layer[material]
    # cut polygon
    p_new = cut_polygon(l.polygon, b_polygon)
    # plot polygon
    plot_polygon(p_new, l.face_color)
    new_layer_name = material + ', ' + ext_label
    l.parent_part.add_new_layer(new_layer_name, p_new, material)
    # write polygon
    part.alt_layer[new_layer_name].write_polygon_edges()

# access the structure for this station
st = station.structure

# upper right -----------------------------------------------------------
label = 'upper right'

# create the bounding polygon
points = [
    (0.0, 0.0),
    (3.0, 0.0),
    (3.0, 3.0),
    (0.0, 3.0)
    ]
bounding_polygon = Polygon(points)
plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'resin', label, 
    bounding_polygon)

# lower right -----------------------------------------------------------
label = 'lower right'

# create the bounding polygon
points = [
    (0.0, 0.0),
    (3.0, 0.0),
    (3.0,-3.0),
    (0.0,-3.0)
    ]
bounding_polygon = Polygon(points)
plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'resin', label, 
    bounding_polygon)

# lower left -----------------------------------------------------------
label = 'lower left'

# create the bounding polygon
points = [
    ( 0.0, 0.0),
    (-3.0, 0.0),
    (-3.0,-3.0),
    ( 0.0,-3.0)
    ]
bounding_polygon = Polygon(points)
plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'resin', label, 
    bounding_polygon)

# lower right -----------------------------------------------------------
label = 'upper left'

# create the bounding polygon
points = [
    ( 0.0, 0.0),
    (-3.0, 0.0),
    (-3.0, 3.0),
    ( 0.0, 3.0)
    ]
bounding_polygon = Polygon(points)
plot_polygon(bounding_polygon, 'None', '#000000')

# cut the new layer polygons
cut_plot_and_write_alt_layer(st.root_buildup, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.external_surface, 'gelcoat', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'triax', label, 
    bounding_polygon)
cut_plot_and_write_alt_layer(st.internal_surface_1, 'resin', label, 
    bounding_polygon)

# show the plot
plt.show()

# write the TrueGrid input file for mesh generation ---------------------------
st.write_truegrid_inputfile(interrupt_flag=True)