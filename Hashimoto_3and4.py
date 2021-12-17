# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:31:53 2021

@author: Hashimoto
"""

import numpy as np
from scipy.signal._peak_finding import argrelmaxequal,argrelminequal
import matplotlib.pyplot as plt

def peak_separate(voltage,current,order):
    max_peaks=argrelmaxequal(current[:,1],order=order)#ピーク検出+の方(自作モジュールなのでargrelmaxで良い)
    min_peaks=argrelminequal(current[:,1],order=order)#ピーク検出-の方(自作モジュールなのでargrelminで良い)
    point=np.sort(np.hstack([max_peaks[0],min_peaks[0]]))#それぞれ検出されたピークを結合
    width=500#ピーク周辺の幅
    data_current=[]#分離電流保存用
    data_voltage=[]#分離電圧保存用
    for i,v in enumerate(point):#pointの数だけfor　enumerateは無くても良い　代用可能
        if (v-width)<=0:#端の処理　左
            data_current.append(current[0:v+width])#電流分離
            data_voltage.append(voltage[0:v+width])#電圧分離
        elif (v+width)>=current[:,0].size:#端の処理　右
            data_current.append(current[v-width:-1])#電流分離
            data_voltage.append(voltage[v-width:-1])#電圧分離
        else:#端の処理しなくてい良い部分
            data_current.append(current[v-width:v+width])#電流分離
            data_voltage.append(voltage[v-width:v+width])#電圧分離
    return data_current,point

voltage_on=np.loadtxt("C12021-11-25-He-1kV-on-100000.txt",skiprows=5)
current_on=np.loadtxt("C22021-11-25-He-1kV-on-100000.txt",skiprows=5)
voltage_off=np.loadtxt("C12021-11-25-He-1kV-off-100000.txt",skiprows=5)
current_off=np.loadtxt("C22021-11-25-He-1kV-off-100000.txt",skiprows=5)
order=1200
separate_current_on,on_point=peak_separate(voltage_on,current_on,order)
separate_current_off,off_point=peak_separate(voltage_off,current_off,order)
#on基準
time_base=voltage_on[1,0]-voltage_on[0,0]
diff_point=on_point-off_point
after_diff_data=[]
for i,v in enumerate(diff_point):
    shift_off=separate_current_off[i]+[v*time_base,0]
    after_diff_data.append([separate_current_on[i][:,0],separate_current_on[i][:,1]-shift_off[:,1]])
after_diff_data=np.hstack(after_diff_data).T
diff=np.setdiff1d(current_on[:,0],after_diff_data[:,0])
current_bool=[]
for i in current_on[:,0]:
    if i in diff:
        current_bool.append(True)
    else:
        current_bool.append(False)
diff_current=current_on[current_bool]
cul_data=np.vstack([diff_current,after_diff_data])
cul_data=cul_data[np.argsort(cul_data[:,0])]
unique=np.unique(cul_data[:,0],return_index =True)[1]
cul_data=cul_data[unique,:]
power=np.stack([voltage_on[:,0],voltage_on[:,1]*cul_data[:,1]],axis=1)
print(sum(power[:,1]*(power[1,0]-power[0,0])))
plt.plot(cul_data[:,0],cul_data[:,1])