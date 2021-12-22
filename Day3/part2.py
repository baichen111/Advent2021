# -*- coding = utf-8 -*-
# @time:12/22/21 6:29 PM
# Author:Bai Chen
# @File:part2.py
# @Software:PyCharm

def day3part2(choice):
    with open("Part2Inputs.txt") as f:
        data = f.read().strip().split()

    for j in range(12):
        c0 = c1 = 0
        ls0 = []
        ls1 = []
        for i in range(len(data)):
            if data[i][j] == "0":
                c0 += 1
                ls0.append(data[i])
            elif data[i][j]== "1":
                c1 += 1
                ls1.append(data[i])
        if choice == "oxygen":
            if c0 > c1:
                data = ls0
            else:
                data = ls1
        elif choice == "co2":
            if c0 > c1:
                data = ls1

            else:
                data = ls0

            if len(data) == 1:
                break;
    return data
if __name__ == '__main__':
    a = int(day3part2("oxygen")[0],2)
    print(a)
    b = int(day3part2("co2")[0],2)
    print(b)
    print(a*b)  #4412188
    #['011001100111']  ['101010000100']
