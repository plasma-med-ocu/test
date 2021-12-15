# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:04:48 2021

@author: Imanaka Kaishu
"""

import numpy as np

V1=np.loadtxt(
    fname="C12021-12-14-He-1kV-10kHz-40-on-100000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

V2=np.loadtxt(
    fname="C12021-12-14-He-1kV-10kHz-40-on-200000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

V3=np.loadtxt(
    fname="C12021-12-14-He-1kV-10kHz-40-on-300000.txt",
    delimiter=",",
    dtype="float",
    skiprows=5 )

V12=np.array((V1[:,0]+V2[:,0],V1[:,1]+V2[:,1])).T

V123=np.array((V12[:,0]+V3[:,0],V12[:,1]+V3[:,1])).T

Vaverage=np.array((V123[:,0]/3,V123[:,1]/3)).T
