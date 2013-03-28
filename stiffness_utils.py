"""
A module to compare the stiffness matrices calculated by VABS and SAFE.

Author: Perry Roth-Johnson
Last updated: March 28, 2013

Usage:
import stiffness_utils as stu
stu.compare_vabs_and_safe(vabs_output_filename='stn26.vabs.K',
                          safe_output_filename='stn26.OUT')

"""

import numpy as np


def compare_vabs_and_safe(vabs_output_filename, safe_output_filename):
    vabs_output_filename = vabs_output_filename
    safe_output_filename = safe_output_filename
    (vabs_output_file, safe_output_file) = _read_files(vabs_output_filename,
                                                       safe_output_filename)
    (K_vabs, K_safe) = _extract_stiffness_matrices(vabs_output_file,
                                                   safe_output_file)
    _print_summary(K_vabs, K_safe)

def _read_files(vabs_output_filename, safe_output_filename):
    """
Read the VABS and SAFE output files into memory.

Returns two lists, which contain all the lines in each file:
(1) vabs_output_file
(2) safe_output_file

    """
    # read the VABS output file into memory
    vof = open(vabs_output_filename, 'r')
    vabs_output_file = vof.readlines()
    vof.close()
    # read the SAFE output file into memory
    sof = open(safe_output_filename, 'r')
    safe_output_file = sof.readlines()
    sof.close()
    return (vabs_output_file, safe_output_file)

def _extract_stiffness_matrices(vabs_output_file, safe_output_file):
    """
Extracts the stiffness matrices calculated by VABS and SAFE.

Returns two numpy arrays, which contain all the coefficients in each stiffness
matrix:
(1) K_vabs
(2) K_safe

    """
    # find the index of the header line for the VABS stiffness matrix
    for i, line in enumerate(vabs_output_file):
        if line == ' Classical Stiffness Matrix (1-extension; 2-twist; 3,4-bending)\n':
            vabs_index = i
    # find the index of the header line for the SAFE stiffness matrix
    for i, line in enumerate(safe_output_file):
        if line == ' STIFFNESS COEFFICIENTS Kappa_I - ORIGINAL COORDINATES\n':
            safe_index = i
    # extract the VABS stiffness matrix
    vabs_stiffness_matrix = vabs_output_file[vabs_index+3:vabs_index+3+4]
    K_vabs = np.zeros((4,4))
    for i, line in enumerate(vabs_stiffness_matrix):
        for j, coeff in enumerate(line.strip().split()):
            K_vabs[i,j] = coeff
    # extract the SAFE stiffness matrix
    safe_stiffness_matrix = safe_output_file[safe_index+2:safe_index+2+4]
    K_safe = np.zeros((4,4))
    for i, line in enumerate(safe_stiffness_matrix):
        for j, coeff in enumerate(line.strip().split()):
            K_safe[i,j] = coeff
    return (K_vabs, K_safe)


def _print_summary(K_vabs, K_safe):
    # print out the results
    sep = 72*'-' + '\n'
    head_fmt = '{0:<26}   {1:<12}   {2:<12}   {3:<13} \n'
    fmt = '{0:<26}   {1:12.6e}   {2:12.6e}   {3:< 12.6%} \n'
    summary = (sep +
               head_fmt.format('stiffness coefficient',
                               'VABS',
                               'SAFE',
                               'percent error') +
               sep +
               fmt.format('bending (about horizontal)',
                          K_vabs[2,2],
                          K_safe[1,1],
                          (K_safe[1,1]-K_vabs[2,2])/K_vabs[2,2]) +
               fmt.format('bending (about vertical)',
                          K_safe[2,2],
                          K_vabs[3,3],
                          (K_safe[2,2]-K_vabs[3,3])/K_vabs[3,3]) +
               fmt.format('extension',
                          K_vabs[0,0],
                          K_safe[0,0],
                          (K_safe[0,0]-K_vabs[0,0])/K_vabs[0,0]) +
               fmt.format('twist',
                          K_vabs[1,1],
                          K_safe[3,3],
                          (K_safe[3,3]-K_vabs[1,1])/K_vabs[1,1]) +
               sep)
    print summary