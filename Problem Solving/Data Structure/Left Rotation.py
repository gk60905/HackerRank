# Link : https://www.hackerrank.com/challenges/array-left-rotation/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    a = deque(a)
    a.rotate(-d)
    print(*list(a))
