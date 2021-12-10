# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:39:34 2021

@author: Imanaka Kaishu
"""

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


V=np.loadtxt(fname="C12021-11-25-He-1kV-on-100000.txt",delimiter="\t",dtype="float",skiprows=5 )

I=np.loadtxt(fname="C22021-11-25-He-1kV-on-100000.txt",delimiter="\t",dtype="float",skiprows=5)

W=np.array([V[:,0],V[:,1]*I[:,1]]).T

w=1250

maxd=signal.argrelmax(I[:,1],order=w)
mind=signal.argrelmin(I[:,1],order=w)


plt.plot(V[:,0],I[:,1],color="black")
plt.scatter(V[:,0][maxd],I[:,1][maxd],color="red")
plt.scatter(V[:,0][mind],I[:,1][mind],color="red")
plt.xlabel("time[s]")
plt.ylabel("current[A]")

s=([I[:979],I[979:2231],I[2231:3467],I[3467:4697],I[4697:5944],I[5944:7196],I[7196:8431],I[8431:]])

plt.plot(s[0][:,0],s[0][:,1])
plt.plot(s[1][:,0],s[1][:,1])
plt.plot(s[2][:,0],s[2][:,1])
plt.plot(s[3][:,0],s[3][:,1])
plt.plot(s[4][:,0],s[4][:,1])
plt.plot(s[5][:,0],s[5][:,1])
plt.plot(s[6][:,0],s[6][:,1])
plt.plot(s[7][:,0],s[7][:,1])