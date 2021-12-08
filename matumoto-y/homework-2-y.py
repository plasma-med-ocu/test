# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:28:11 2021

@author: Owner
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt                                            
    
V = np.loadtxt(
       fname="C12021-11-25-He-1kV-on-100000.txt" ,
       dtype="float" ,
       delimiter="\t" ,
       skiprows=5 ,
       )

I = np.loadtxt(
       fname="C22021-11-25-He-1kV-on-100000.txt" ,
       dtype="float" ,
       delimiter="\t" ,
       skiprows=5 ,
       )

w = 1200

peaks1 = signal.argrelmax(I[:,1], order=w)
peaks2 = signal.argrelmin(I[:,1], order=w)

plt.plot(I[:,0], I[:,1], color='black')
plt.xlabel("Time(s)")
plt.ylabel("Current(A)")
plt.plot(I[:,0][peaks1], I[:,1][peaks1],"ro")
plt.plot(I[:,0][peaks2], I[:,1][peaks2],"bo")


Is = np.split(I, [977,1982,2481,3453,4453,4941,5947,6947,7445,8417,9417])

print(Is)