# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:19:19 2021

@author: Imanaka Kaishu
"""

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

I_on=np.loadtxt(
    fname="C22021-11-25-He-1kV-on-100000.txt",
    delimiter="\t",
    dtype="float",
    skiprows=5 )

I_off=np.loadtxt(
    fname="C22021-11-25-He-1kV-off-100000.txt",
    delimiter="\t",
    dtype="float",
    skiprows=5)

w_on=1250

maxd_on=signal.argrelmax(I_on[:,1],order=w_on)
mind_on=signal.argrelmin(I_on[:,1],order=w_on)

peak_on= []
for i in maxd_on[0]:
    peak_on.append(i)
    
for i in mind_on[0]:
    peak_on.append(i)
peak_on = sorted(peak_on)
print(peak_on)

plt.plot(I_on[:,0],I_on[:,1],color="black")
plt.scatter(I_on[:,0][maxd_on],I_on[:,1][maxd_on],color="red")
plt.scatter(I_on[:,0][mind_on],I_on[:,1][mind_on],color="red")
plt.xlabel("time[s]")
plt.ylabel("current[A]")

w_off=1250

maxd_off=signal.argrelmax(I_off[:,1],order=w_off)
mind_off=signal.argrelmin(I_off[:,1],order=w_off)

peak_off= []
for i in maxd_off[0]:
    peak_off.append(i)
    
for i in mind_off[0]:
    peak_off.append(i)
peak_off = sorted(peak_off)
print(peak_off)


dxdy_off = []
for peak in peak_off[1:]:
    d, etc = signal.phaseCorrelate(peak, peak_off[0])   
    dx, dy = d
    dxdy_off.append([dx, dy])
    
rows, cols = peak_off[0].shape
peak_after_off = [peak_off[0]]
for dxdy, peak in zip(dxdy_off, peak_off[1:]):
    dx, dy = dxdy
    M = signal.float32([[1, 0, dx],[0, 1, dy]])
    peak = np.warpAffine(peak, M, (cols,rows))
    peak_after_off.append(peak)
    
fig = plt.figure(figsize = (6, 6))    

subplot_off = [477, 1483, 2981, 3954, 5442, 6448, 7946, 8918]
for subplot, peak in zip(subplot_off, peak_off):
    ax = fig.add_subplot(subplot)
    ax.imshow(peak)

subplot_after_off = [477, 1482, 2981, 3953, 5441, 6447, 7945, 8917]
for subplot_after, peak_after in zip(subplot_after_off, peak_after_off):
    ax = fig.add_subplot(subplot_after)
    ax.imshow(peak_after)

plt.savefig('test.png', format = 'png', dpi=1250)
plt.show()

plt.plot(I_off[:,0],I_off[:,1],color="black")
plt.scatter(I_off[:,0][maxd_off],I_off[:,1][maxd_off],color="blue")
plt.scatter(I_off[:,0][mind_off],I_off[:,1][mind_off],color="blue")
plt.xlabel("time[s]")
plt.ylabel("current[A]")