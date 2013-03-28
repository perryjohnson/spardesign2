import vabs_utils as vu
import safe_utils as su


fv = vu.VabsInputFile(
     vabs_filename='stn26.vabs',
     grid_filename='stn26.abq')

fs = su.SafeInputFile(
     title='blade station 26',
     safe_filename='stn26.safe',
     grid_filename='stn26.abq')