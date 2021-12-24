# -*- coding = utf-8 -*-
# @time:12/22/21 10:01 PM
# Author:Bai Chen
# @File:part1.py
# @Software:PyCharm
import numpy as np

def checkMatrix(m):
    for r in m:
        if set(r) == {1}:
            return True
    for c in np.transpose(m):
        if set(c) == {1}:
            return True
    return False

def runMatrix(ar,mark):
    for v in nums:
        for i in range(len(ar)):
            for j in range(len(ar[i])):
                for k in range(len(ar[i][j])):
                    if checkMatrix(mark[i]):
                        return  v,ar[i],mark[i]
                    if ar[i][j][k] == v:
                        mark[i][j][k] = 1


if __name__ == '__main__':
    #load data
    with open("Part1Inputs.txt") as f:
        data = f.read().strip().split("\n")
    #load first line of data
    nums = []
    ls = data[0].split(",")
    for x in ls:
        nums.append(int(x))

    #make matrix
    new_ls = []
    outer = []
    for x in data[2:]:
        string_nums = x.split()
        if string_nums == []:
            outer.append(new_ls)
            new_ls = []
        else:
            inner = [int(v) for v in string_nums]
            new_ls.append(inner)
    outer.append(new_ls)

    ar = np.array(outer)  #convert nested list to numpy array

    mark = np.zeros(ar.shape,dtype=int)

    num,fin_array,fin_mark = runMatrix(ar,mark)
    print(num*sum(fin_array[np.where(fin_mark == 0)])) # 58374 final answer









