# Link : https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def check_prime(s):
    if s == 1:
        return('Not prime')
    sqrt = int(math.sqrt(s))
    for j in range(2,sqrt+1):
        if s%j == 0:
            return('Not prime')
    return('Prime')

N = int(input())
for i in range(N):
    s = int(input())
    print(check_prime(s))