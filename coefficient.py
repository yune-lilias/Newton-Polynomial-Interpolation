import math
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def newploy(inputtype, in_x, in_y):
   #if input type is 0, then the input y is a function
   if inputtype == 0:
      in_y = in_y(in_x)
   F = np.zeros([len(in_x),len(in_x)])  
   F[:,0] = in_y
   for i in range(1,len(in_x)):
      for j in range(1,i+1):
         F[i,j] = (F[i,j-1]-F[i-1,j-1])/(in_x[i]-in_x[i-j])
   return F.diagonal()

 
