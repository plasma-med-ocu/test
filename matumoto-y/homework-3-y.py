# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:42:56 2021

@author: Owner
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt 

Ion = np.loadtxt(fname="C22021-11-25-He-1kV-on-100000.txt" ,dtype="float" ,
       delimiter="\t" , skiprows=5 ,)

Ioff = np.loadtxt(fname="C22021-11-25-He-1kV-off-100000.txt" ,dtype="float" ,
       delimiter="\t" , skiprows=5 ,)

#Ion
w = 1200

peaks1 = signal.argrelmax(Ion[:,1], order=w)
peaks2 = signal.argrelmin(Ion[:,1], order=w)

peak = []
for i in peaks1[0]:
    peak.append(i)
    
for i in peaks2[0]:
    peak.append(i)
peak = sorted(peak)

plt.plot(Ion[:,0], Ion[:,1], color='black')
plt.scatter(Ion[:,0][peaks1], Ion[:,1][peaks1],c = 'b')
plt.scatter(Ion[:,0][peaks2], Ion[:,1][peaks2],c = 'b')
plt.xlabel("Time(s)")
plt.ylabel("Current(A)")

peakpeak = [(peak[i]+peak[i+1])//2 for i in range(len(peak)-1)]

Is = np.split(Ion, peakpeak)

for i in range(len(peak)):
    plt.plot(Is[i][:,0],Is[i][:,1])

#Ioff
w = 1200

peaks3 = signal.argrelmax(Ioff[:,1], order=w)
peaks4 = signal.argrelmin(Ioff[:,1], order=w)

peaks = []
for i in peaks3[0]:
    peaks.append(i)
    
for i in peaks4[0]:
    peaks.append(i)
peaks = sorted(peaks)

plt.figure()
plt.plot(Ioff[:,0], Ioff[:,1], color='black')
plt.scatter(Ioff[:,0][peaks3], Ioff[:,1][peaks3],c = 'r')
plt.scatter(Ioff[:,0][peaks4], Ioff[:,1][peaks4],c = 'r')
plt.xlabel("Time(s)")
plt.ylabel("Current(A)")

peakspeaks = [(peaks[i]+peaks[i+1])//2 for i in range(len(peaks)-1)]

Iss = np.split(Ioff, peakspeaks)

for i in range(len(peaks)):
    plt.plot(Iss[i][:,0],Iss[i][:,1])

#peakawase-sabunn
plt.figure()
Ipla = []
for i in range(len(peaks)):
    if peak[i] == peaks[i]:
       if len(Is[i]) > len(Iss[i]):
         Ipla.append(Is[i][0:-1,1] - Iss[i][:,1])
         plt.plot(Is[i][0:-1,0],Ipla[i])
       elif len(Is[i]) <= len(Iss[i]):
         Ipla.append(Is[i][:,1] - Iss[i][0:-1,1])
         plt.plot(Is[i][:,0],Ipla[i])
    elif len(Is[i]) == len(Iss[i]):
        np.roll(Iss,1)
        Ipla.append(Is[i][:,1] - Iss[i][:,1])
        plt.plot(Is[i][:,0],Ipla[i])
    elif len(Is[i]) < len(Iss[i]):
        np.roll(Iss,1)
        Ipla.append(Is[i][:,1] - Iss[i][1:,1])
        plt.plot(Is[i][:,0],Ipla[i])
    elif len(Is[i]) > len(Iss[i]):
        np.roll(Iss,1)
        Ipla.append(Is[i][0:-2,1] - Iss[i][1:,1])
        plt.plot(Is[i][0:-2,0],Ipla[i])
        

