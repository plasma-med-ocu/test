# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:28:11 2021

@author: Owner
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt                                            

'''    
V = np.loadtxt(
       fname="C12021-11-25-He-1kV-on-100000.txt" ,
       dtype="float" ,
       delimiter="\t" ,
       skiprows=5 ,
       )
'''

I = np.loadtxt(
       fname="C22021-11-25-He-1kV-on-100000.txt" ,
       dtype="float" ,
       delimiter="\t" ,
       skiprows=5 ,
       )

w = 1200
#w = int(input('w='))


peaks1 = signal.argrelmax(I[:,1], order=w)
peaks2 = signal.argrelmin(I[:,1], order=w)

peak = []
for i in peaks1[0]:
    peak.append(i)
    
for i in peaks2[0]:
    peak.append(i)
peak = sorted(peak)
print(peak)

plt.plot(I[:,0], I[:,1], color='black')
plt.scatter(I[:,0][peaks1], I[:,1][peaks1],c = 'r')
plt.scatter(I[:,0][peaks2], I[:,1][peaks2],c = 'b')
plt.xlabel("Time(s)")
plt.ylabel("Current(A)")

peakpeak = [(peak[i]+peak[i+1])//2 for i in range(len(peak)-1)]
    
print(peakpeak)

Is = np.split(I, peakpeak)

for i in range(len(peak)):
    plt.plot(Is[i][:,0],Is[i][:,1])



