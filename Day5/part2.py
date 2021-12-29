# -*- coding = utf-8 -*-
# @time:12/29/21 12:41 PM
# Author:Bai Chen
# @File:part2.py
# @Software:PyCharm


def lin(x1,y1,x2,y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a*x1
    return a,b

if __name__ == '__main__':
    with open("part2inputs.txt") as f:
        data = f.read().strip().split()

    ls = list(filter(lambda x: x != "->"  ,data))
    nums = list(map(lambda x:[int(i) for i in x.split(",")],ls))
    pairs = []
    for i in range(0,len(nums)-1,2):
        pairs.append([nums[i],nums[i+1]])

    #pairs = [[[0, 9], [5, 9]],[[8, 0], [0, 8]],[[9, 4], [3, 4]],[[2, 2], [2, 1]],[[7, 0], [7, 4]],[[6, 4], [2, 0]],[[0, 9], [2, 9]],[[3, 4], [1, 4]],[[0, 0], [8, 8]],[[5, 5], [8, 2]]]
    # logic body:
    d = {}
    for pair in pairs:    #pair : [[299, 462], [299, 747]]
        x1 = pair[0][0]; y1 = pair[0][1]; x2 = pair[1][0]; y2 = pair[1][1]
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        if x1 == x2:
            for v in range(min_y,max_y + 1):
                k = (x1,v)
                if k not in d:
                    d[k] = 0
                d[k] += 1
        elif y1 == y2:
            for v in range(min_x,max_x + 1):
                k = (v,y1)
                if k not in d:
                    d[k] = 0
                d[k] += 1
        elif max_x - min_x == max_y - min_y:
            a, b = lin(x1,y1,x2,y2)          #linear equation
            for x in range(min_x,max_x + 1):
                y = x*a + b
                k = (x,y)
                if k not in d:
                    d[k] = 0
                d[k] += 1
    s = 0
    for k,v in d.items():
        if v >= 2:
            s += 1

    print(s)   # 18144 final answer
