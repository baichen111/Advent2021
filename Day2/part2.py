# -*- coding = utf-8 -*-
# @time:12/22/21 9:14 PM
# Author:Bai Chen
# @File:part2.py
# @Software:PyCharm

if __name__ == '__main__':
    with open("Part2Inputs.txt") as f:
        data = f.read().strip().split()
    dir = []
    nums = []
    for x in data:
        if x in ["forward","up","down"]:
            dir.append(x)
        else:
            nums.append(int(x))

    n = len(dir)
    depth = 0
    hor = 0
    aim = 0
    for i in range(n):
        if dir[i] == "forward":
            hor += nums[i]
            depth += nums[i]*aim
        if dir[i] == "down":
            aim += nums[i]
        if dir[i] == "up":
            aim -= nums[i]
    print(hor,depth)
    print(hor*depth)



