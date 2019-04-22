# Link : https://www.hackerrank.com/challenges/30-regex-patterns/problem


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    stack = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        check_gmail = re.findall('@gmail.com$', emailID)
        if (check_gmail):
            stack.append(firstName)
    stack.sort()
    for elm in stack:
        print(elm)