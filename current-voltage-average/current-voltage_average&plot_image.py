# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:16:45 2021

@author: Imanaka Kaishu
"""

import numpy as np
from matplotlib import pyplot as plt

V1=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C12021-12-15-He-1kV-10kHz-30%-on-100000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

V2=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C12021-12-15-He-1kV-10kHz-30%-on-200000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

V3=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C12021-12-15-He-1kV-10kHz-30%-on-300000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

V12=np.array((V1[:,0]+V2[:,0],V1[:,1]+V2[:,1])).T

V123=np.array((V12[:,0]+V3[:,0],V12[:,1]+V3[:,1])).T

Vaverage=np.array((V123[:,0]/3,V123[:,1]/3)).T

np.savetxt(
    "C:/python/test/current-voltage-average/30%/C12021-He-1kV-10kHz-30%-average.txt",
    Vaverage,
    delimiter=",",
    )

plt.plot(Vaverage[:,0],Vaverage[:,1])



I1=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-100000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

I2=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-200000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

I3=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-300000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

I12=np.array((I1[:,0]+I2[:,0],I1[:,1]+I2[:,1])).T

I123=np.array((I12[:,0]+I3[:,0],I12[:,1]+I3[:,1])).T

Iaverage=np.array((I123[:,0]/3,I123[:,1]/3)).T

np.savetxt(
    "C:/python/test/current-voltage-average/30%/C22021-He-1kV-10kHz-30%-average.txt",
    Iaverage,
    delimiter=",",
    )

plt.plot(Iaverage[:,0],Iaverage[:,1])