import itertools
import pickle
import numpy as np

import DefineParts

## メイン処理
# 軽量化を最大化
# ブレーキ90以上

with open('generate.pb','rb') as f:
    out = pickle.load(f)

temp = 0
name = ""
for i in out:
    if(i.brake >= 90):
        if(i.lightweight > temp):
            temp = i.lightweight
            name = i.name
            print(i.name, i.power, i.aero, i.lightweight, i.handling, i.brake, i.point)
#print(name, temp)

print("-------")
# ブレーキ90以上の条件を除外してみる
temp = 0
name = ""
for i in out:
    if(i.lightweight > temp):
        temp = i.lightweight
        name = i.name
        print(i.name, i.power, i.aero, i.lightweight, i.handling, i.brake, i.point)


#arr_out = np.array(out)
#print(arr_out.max())
