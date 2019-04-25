# Link :https://www.hackerrank.com/challenges/crush/problem

n,m =[int(x) for x in input().split()]
aa=[0]* (n+1)
for _ in range(m):
    a,b,x = [int(xx) for xx in input().split()]
    aa[a-1]+=x
    if((b)<=len(aa)):
        aa[b]-=x
max = a = 0
for i in aa:
   a=a+i;
   if(max<a): max=a;
print(max)