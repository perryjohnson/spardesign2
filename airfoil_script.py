import airfoil_utils as afu
reload(afu)
a = afu.Airfoil('NACA 64-618','SNL100-00_v0/airfoils/NACA_64-618.txt')
a.plot_all_segments()

# write the segments to a file, segments.tg ----------------------------------
f = open('segments.tg','w+')

def write_segment(f,segment,segment_name,curve_number,comments='c'):
    """Write a segment to a file, formatted as a 2D curve for a TrueGrid input file.

    """
    f.write(comments + ' ' + segment_name + '\n')
    f.write('ld ' + str(curve_number) + ' lp2' + '\n')
    fmt = '{0:> 10.8f}' + '{1:> 14.8f}' + '\n'
    for coord in segment:
        f.write(fmt.format(coord['x'], coord['y']))
    f.write(';\n\n')

# Write all the segments extracted from the airfoil to a TrueGrid input file.
curve_id = 1
write_segment(f,a.TE_lower_sharp_segment,'trailing edge reinforcement, lower sharp segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.TE_lower_main_segment,'trailing edge reinforcement, lower main segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.aft_panel_lower_segment,'aft panel, lower segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.rear_SW_lower_segment,'rear shear web, lower segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.SC_lower_segment,'spar cap, lower segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.fwd_SW_lower_segment,'forward shear web, lower segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.LE_segment,'leading edge panel, segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.fwd_SW_upper_segment,'forward shear web, upper segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.SC_upper_segment,'spar cap, upper segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.rear_SW_upper_segment,'rear shear web, upper segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.aft_panel_upper_segment,'aft panel, upper segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.TE_upper_main_segment,'trailing edge reinforcement, upper main segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.TE_upper_sharp_segment,'trailing edge reinforcement, upper sharp segment', curve_id)
curve_id = curve_id + 1
write_segment(f,a.TE_inner_surf_segment,'trailing edge reinforcement, inner surface', curve_id)

def write_segment_from_coords(f,list_of_coords,segment_name,curve_number,comments='c'):
    """
Write a list of coords to a file, formatted as a 2D curve for a TrueGrid input file.

    """
    f.write(comments + ' ' + segment_name + '\n')
    f.write('ld ' + str(curve_number) + ' lp2' + '\n')
    fmt = '{0:> 10.8f}' + '{1:> 14.8f}' + '\n'
    for coord in list_of_coords:
        f.write(fmt.format(coord[0], coord[1]))
    f.write(';\n\n')

# draw guide curves for the shear webs
#   forward shear web
curve_id = 23
write_segment_from_coords(f,a.fwd_SW_left_coords,'forward shear web, left segment', curve_id)
curve_id = curve_id + 1
write_segment_from_coords(f,a.fwd_SW_right_coords,'forward shear web, right segment', curve_id)
#   rear shear web
curve_id = curve_id + 1
write_segment_from_coords(f,a.rear_SW_left_coords,'rear shear web, left segment', curve_id)
curve_id = curve_id + 1
write_segment_from_coords(f,a.rear_SW_right_coords,'rear shear web, right segment', curve_id)
#  foward shear web, foam core
curve_id = curve_id + 1
write_segment_from_coords(f,a.fwd_SW_foam_left_coords,'forward shear web, foam core, left segment', curve_id)
curve_id = curve_id + 1
write_segment_from_coords(f,a.fwd_SW_foam_right_coords,'forward shear web, foam core, right segment', curve_id)
#  rear shear web, foam core
curve_id = curve_id + 1
write_segment_from_coords(f,a.rear_SW_foam_left_coords,'rear shear web, foam core, left segment', curve_id)
curve_id = curve_id + 1
write_segment_from_coords(f,a.rear_SW_foam_right_coords,'rear shear web, foam core, right segment', curve_id)

# close the file
f.close()
