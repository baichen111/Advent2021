# -*- coding = utf-8 -*-
# @time:12/27/21 7:27 AM
# Author:Bai Chen
# @File:part1.py
# @Software:PyCharm

if __name__ == '__main__':
    with open("part1inputs.txt") as f:
        data = f.read().strip().split()

    m = []
    for x in data:
        m.append([int(v) for v in list(x)])

    dp = [[0]*len(m[0]) for x in range(len(m))]

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] += m[i][j]
            if i > 0 and j > 0 :
                dp[i][j] += min(dp[i][j-1],dp[i-1][j])
            elif i > 0 :
                dp[i][j] += dp[i-1][j]
            elif j > 0:
                dp[i][j] += dp[i][j-1]

    print(dp[99][99] - m[0][0])   #811