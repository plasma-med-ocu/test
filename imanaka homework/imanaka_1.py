# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:10:20 2021

@author: Imanaka Kaishu
"""

import numpy as np

x=np.loadtxt("C12021-11-25-He-1kV-on-100000.txt",delimiter=" ",dtype="int")

y=np.loadtxt("C22021-11-25-He-1kV-on-100000.txt",delimiter=" ",dtype="int")

np.array([x,y])

print(x)
print(y)

result=x*y

print(result)


