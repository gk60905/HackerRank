# Link : https://www.hackerrank.com/challenges/30-nested-logic/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

Da, Ma, Ya = input().split()
Da, Ma, Ya = int(Da), int(Ma), int(Ya)
De, Me, Ye = input().split()
De, Me, Ye = int(De), int(Me), int(Ye)
dDiff, mDiff, yDiff = (Da - De), (Ma - Me), (Ya - Ye)

if ((Ma == Me) and (Ya == Ye)):
    Fine = 15 * (dDiff)
    print(Fine)
elif ((mDiff > 0) and (Ya == Ye)):
    Fine = 500 * (mDiff)
    print(Fine)
elif (yDiff > 0):
    Fine = 10000
    print(Fine)
else:
    print(0)