# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:39:34 2021

@author: Imanaka Kaishu
"""

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt


V=np.loadtxt(fname="C:/python/test/current-voltage-average/30%/C12021-12-15-He-1kV-10kHz-30%-on-100000.txt",delimiter=",",dtype="float",skiprows=5 )

I=np.loadtxt(fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-100000.txt",delimiter=",",dtype="float",skiprows=5)

W=np.array([V[:,0],V[:,1]*I[:,1]]).T

w=12500

maxd=signal.argrelmax(I[:,1],order=w)
mind=signal.argrelmin(I[:,1],order=w)


plt.plot(V[:,0],I[:,1],color="black")
plt.scatter(V[:,0][maxd],I[:,1][maxd],color="red")
plt.scatter(V[:,0][mind],I[:,1][mind],color="red")
plt.xlabel("time[s]")
plt.ylabel("current[A]")

