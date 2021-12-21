# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:04:48 2021

@author: Imanaka Kaishu
"""

import numpy as np
from matplotlib import pyplot as plt

sample1=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-100000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

sample2=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-200000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

sample3=np.loadtxt(
    fname="C:/python/test/current-voltage-average/30%/C22021-12-15-He-1kV-10kHz-30%-on-300000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

sample12=np.array((sample1[:,0]+sample2[:,0],sample1[:,1]+sample2[:,1])).T

sample123=np.array((sample12[:,0]+sample3[:,0],sample12[:,1]+sample3[:,1])).T

sample_average=np.array((sample123[:,0]/3,sample123[:,1]/3)).T

np.savetxt(
    "C:/python/test/current-voltage-average/30%/C22021-He-1kV-10kHz-30%-average.txt",
    sample_average,
    delimiter=",",
    )

plt.plot(sample_average[:,0],sample_average[:,1])

