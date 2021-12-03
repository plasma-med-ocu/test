# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:46:06 2021

@author: Hashimoto
"""
import numpy as np
voltage=np.loadtxt("C12021-11-25-He-1kV-on-100000.txt",skiprows=5)
current=np.loadtxt("C22021-11-25-He-1kV-on-100000.txt",skiprows=5)
power=np.stack([voltage[:,0],voltage[:,1]*current[:,1]],axis=1)
print(sum(power[:,1]*(power[1,0]-power[0,0])))

#list
#基本のデータ格納型　インデックス
a=[[1,2,3,4],[5,6,7,8]]
print(a[1][2])
aa=[1,2.3,"4"]
print(aa)

#set
#集合型　重複要素削除 集合演算　更新不可(追加、削除は可能)
b={1,2,3,4,4,4,4,4,4}
print(b)

#tuple
#要素の変更が出来ないデータ型　演算が少し速い
c=((1,2,3,4),(5,6,7,8))
print(c[1][2])

#dictionary
#keyを使ってわかりやすくする keyとvalueがセットになっている
d={"apple":1, "orange":2, "banana":3}
print(d["apple"])

#pandas
import pandas as pd
df=pd.read_csv("C12021-11-25-He-1kV-on-100000.txt",header=4,sep="\t")
print(df["Time"])


#numpy
print(power[2:7,1])
print(power[power[:,1]>0])