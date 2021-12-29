# -*- coding = utf-8 -*-
# @time:12/29/21 10:06 AM
# Author:Bai Chen
# @File:part1.py
# @Software:PyCharm


if __name__ == '__main__':
    with open("part1inputs.txt") as f:
        data = f.read().strip().split()

    ls = list(filter(lambda x: x != "->"  ,data))
    nums = list(map(lambda x:[int(i) for i in x.split(",")],ls))
    pairs = []
    for i in range(0,len(nums)-1,2):
        pairs.append([nums[i],nums[i+1]])

    #pairs = [[[0, 9], [5, 9]],[[8, 0], [0, 8]],[[9, 4], [3, 4]],[[2, 2], [2, 1]],[[7, 0], [7, 4]],[[6, 4], [2, 0]],[[0, 9], [2, 9]],[[3, 4], [1, 4]],[[0, 0], [8, 8]],[[5, 5], [8, 2]]]

    d = {}
    for pair in pairs:    #pair : [[299, 462], [299, 747]]
        x1 = pair[0][0]; y1 = pair[0][1]; x2 = pair[1][0]; y2 = pair[1][1]
        if x1 == x2:
            min_y = min(y1,y2)
            max_y = max(y1,y2)
            for v in range(min_y,max_y + 1):
                k = (x1,v)
                if k not in d:
                    d[k] = 0
                d[k] += 1
        elif y1 == y2:
            min_x = min(x1,x2)
            max_x = max(x1,x2)
            for v in range(min_x,max_x + 1):
                k = (v,y1)
                if k not in d:
                    d[k] = 0
                d[k] += 1
    s = 0
    for k,v in d.items():
        if v >= 2:
            s += 1

    print(s)  #5576










