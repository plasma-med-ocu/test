# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:16:59 2021

@author: Owner
"""

import numpy as np

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

W = np.array([V[:,0], V[:,1]*I[:,1]])

Wtr = W.T

print(Wtr)










