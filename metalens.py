
from rstools import *
from math import *

def rsoft_main(ind_file='',
               diameter_ratio_file='',
               Period=0.24,
               D=10):

  # create a circuit
  c=RSoftCircuit()

  # set symbols
  c.set_symbol('Thickness', 1)
  c.set_exports('Thickness')

  # read data file
  diameter_ratio_data = RSoftUserFunction()
  diameter_ratio_data.read(diameter_ratio_file)
  
  # calculate array dimension
  N = 2*int((D/2)/Period)+1

  # build metalens
  for i in range(N):
    for j in range(N):
      x = (i-(N-1)/2)*Period
      y = (j-(N-1)/2)*Period
      r = sqrt(x**2+y**2)
      ratio = diameter_ratio_data.eval(r)
      c.add_segment( (x,y,0), (0,0,'Thickness'), (ratio*Period, ratio*Period) )

  # save circuit to file
  c.write(ind_file)

