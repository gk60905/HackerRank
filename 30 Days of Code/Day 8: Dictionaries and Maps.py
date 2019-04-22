# Link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
phoneBook = dict()
for i in range(N):
    name, phone = input().split()
    phone = int(phone)
    phoneBook[name] = phone

while(True):
    try:
        check_name = input()
        if check_name in phoneBook:
            print('{}={}'.format(check_name, phoneBook[check_name]))
        else:
            print('Not found')
    except:
        break


