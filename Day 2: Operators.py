#!/bin/python3
# Link : https://www.hackerrank.com/challenges/30-operators/problem

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost + (meal_cost*(round((tip_percent/100), 2))) + (meal_cost*(round((tax_percent/100), 2)))))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
