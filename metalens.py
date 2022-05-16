
from rstools import *
from math import *

def rsoft_main(ind_file=''):

  # create a circuit
  c=RSoftCircuit()
  array=[
    0.168,
    0.167,
    0.165,
    0.163,
    0.161,
    0.157,
    0.154,
    0.149,
    0.144,
    0.138,
    0.132,
    0.124,
    0.114,
    0.101,
    0.081,
    0.22,
    0.209,
    0.2,
    0.19,
    0.181,
    0.17,
    0.158,
    0.145,
    0.131,
    0.112,
    0.083,
    0.213,
    0.199,
    0.185,
    0.17]
  Period=0.25
  c.add_segment( (0,0,0.5), (0,0,1.1), (0.169, 0.169) )
  for i in range(len(array)):
    x = (i+1)*Period
    c.add_segment( (x,0,0.5), (0,0,1.1), (array[i], array[i]) )
    c.add_segment((-x, 0, 0.5), (0, 0, 1.1), (array[i], array[i]))

  # save circuit to file
  c.write(ind_file)

