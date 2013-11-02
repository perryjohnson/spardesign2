import os
import matplotlib.pyplot as plt
import numpy as np
import lib.blade as bl
reload(bl)

# load the sandia blade
m = bl.MonoplaneBlade('Sandia blade SNL100-00', 'sandia_blade',
    rotate_airfoil_coords=False)

# pre-process the airfoil coordinates
station = m.list_of_stations[22]
# for station in m.list_of_stations:
station.airfoil.create_polygon()
station.structure.create_all_layers()
station.structure.save_all_layer_edges()
station.structure.create_all_alternate_layers()
station.structure.save_all_alternate_layer_edges()

station.plot_parts(alternate_layers=True)

# stn16 = m.list_of_stations[15]
# stn16.plot_parts()
# f = stn16.structure.TE_reinforcement.layer['foam']
# u = stn16.structure.TE_reinforcement.layer['uniax']
