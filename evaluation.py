import math
import numpy as np
 
def neweva(coe,in_x,x):
   sum = 0
   for i in range(len(coe)):
     prod = 1
     for j in range(i):
       prod *= (x - in_x[j])
     sum += coe[i]*prod
   return sum


def neweva2(coe,in_x):
   res = '0'
   for i in range(len(coe)):
     prod = str(1)
     for j in range(i):
       prod = '(x- '+ str(in_x[j]) + ')*' + prod
     res = res + '+' +str(coe[i]) + '*' + prod
   return res
