import sys

num_str = sys.stdin.readline().rstrip()

numbers = [int(i) for i in num_str]

to_one = 0
to_zero = 0

now_one = False
for i in numbers:
    if (i == 0 and now_one == True):
        to_one +=1
        now_one = False
    elif (i==1):
        now_one = True

if(now_one == True):
    to_one +=1

numbers = [int(i) for i in num_str]
now_zero =False
for i in numbers:
    if(i==1 and now_zero == True):
        to_zero +=1
        now_zero = False
    elif (i==0):
        now_zero = True

if (now_zero == True):
    to_zero += 1

if(to_zero>to_one):
    print(to_one)
else:
    print(to_zero)
