# Link : https://www.hackerrank.com/challenges/30-bitwise-and/problem


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        # Brute Force Method (take long long time)
        n = range(1,n+1)
        max_value = []
        count = []
        for i in range(len(n)):
            for j in range(i+1, len(n)): 
                count.append(n[i] & n[j])

        for i in count:
            if i < k:
                max_value.append(i)

        print(max(max_value))


# O(n) Method (Simply Wow!!)
# print(k-1 if ((k-1) | k) <= n else k-2)