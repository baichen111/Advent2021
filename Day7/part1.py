# -*- coding = utf-8 -*-
# @time:12/25/21 11:19 AM
# Author:Bai Chen
# @File:part1.py
# @Software:PyCharm
import numpy as np


if __name__ == '__main__':
    with open("Part1Inputs.txt") as f:
        data = f.read().strip().split()

    data= data[0].split(",")
    nums = []
    for x in data:
        nums.append(int(x))
    nums_np = np.array(nums)
    minimum = float("inf")
    for v in nums_np:
        dif = np.abs(nums_np - v)
        s = sum(dif)
        if s < minimum:
            minimum = s
    print(minimum)  #326132 final answer
