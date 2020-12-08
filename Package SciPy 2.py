#https://www.w3schools.com/python/scipy_optimizers.asp

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)