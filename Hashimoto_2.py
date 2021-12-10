# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:46:06 2021

@author: Hashimoto
"""
import numpy as np
voltage=np.loadtxt("C12021-11-25-He-1kV-on-100000.txt",skiprows=5)
current=np.loadtxt("C22021-11-25-He-1kV-on-100000.txt",skiprows=5)
power=np.stack([voltage[:,0],voltage[:,1]*current[:,1]],axis=1)
#ここまでは前回分
from scipy.signal._peak_finding import argrelmaxequal,argrelminequal
import matplotlib.pyplot as plt
max_peaks=argrelmaxequal(current[:,1],order=1000)#ピーク検出+の方(自作モジュールなのでargrelmaxで良い)
min_peaks=argrelminequal(current[:,1],order=1200)#ピーク検出-の方(自作モジュールなのでargrelminで良い)
plt.plot(current[:,0],current[:,1])#電流波形確認用プロット(直線)
point=np.sort(np.hstack([max_peaks[0],min_peaks[0]]))#それぞれ検出されたピークを結合
sct=current[point,:]#ピークに相当する電流を取得
plt.scatter(sct[:,0],sct[:,1])#ピークをプロット(散布図)
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
for i in range(len(data_current)):
    plt.plot(data_current[i][:,0],data_current[i][:,1])#最終結果プロット(直線)

#普通は以下で十分対応可能
"""
for v in point:
    print(v)
"""
#デフォルトではインライン表示になっている