# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:55:55 2021

@author: Imanaka Kaishu
"""

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

V=np.loadtxt(
    fname="C12021-11-25-He-1kV-on-100000.txt",
    delimiter="\t",
    dtype="float",
    skiprows=5 )

I=np.loadtxt(
    fname="C22021-11-25-He-1kV-on-100000.txt",
    delimiter="\t",
    dtype="float",
    skiprows=5)

W=np.array([V[:,0],V[:,1]*I[:,1]]).T

w=1250

maxd=signal.argrelmax(I[:,1],order=w)
mind=signal.argrelmin(I[:,1],order=w)

peak= []
for i in maxd[0]:
    peak.append(i)
    
for i in mind[0]:
    peak.append(i)
peak = sorted(peak)
print(peak)

plt.plot(V[:,0],I[:,1],color="black")
plt.scatter(V[:,0][maxd],I[:,1][maxd],color="red")
plt.scatter(V[:,0][mind],I[:,1][mind],color="red")
plt.xlabel("time[s]")
plt.ylabel("current[A]")

separate=[]
for i in range(len(peak)-1):
    average=(peak[i]+peak[i+1])//2
    separate.append(average)
    
print(average)

Iseparate1=np.split(I,separate)

for i in range(len(peak)):
    plt.plot(Iseparate1[i][:,0],Iseparate1[i][:,1])
    
    
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

V=np.loadtxt(
    fname="C12021-11-25-He-1kV-off-100000.txt",
    delimiter="\t",
    dtype="float",
    skiprows=5 )

I=np.loadtxt(
    fname="C22021-11-25-He-1kV-off-100000.txt",
    delimiter="\t",
    dtype="float",
    skiprows=5)

W=np.array([V[:,0],V[:,1]*I[:,1]]).T

w=1250

maxd=signal.argrelmax(I[:,1],order=w)
mind=signal.argrelmin(I[:,1],order=w)

peak= []
for i in maxd[0]:
    peak.append(i)
    
for i in mind[0]:
    peak.append(i)
peak = sorted(peak)
print(peak)

plt.plot(V[:,0],I[:,1],color="black")
plt.scatter(V[:,0][maxd],I[:,1][maxd],color="blue")
plt.scatter(V[:,0][mind],I[:,1][mind],color="blue")
plt.xlabel("time[s]")
plt.ylabel("current[A]")

separate=[]
for i in range(len(peak)-1):
    average=(peak[i]+peak[i+1])//2
    separate.append(average)
    
print(average)

Iseparate2=np.split(I,separate)

for i in range(len(peak)):
    plt.plot(Iseparate2[i][:,0],Iseparate2[i][:,1])


