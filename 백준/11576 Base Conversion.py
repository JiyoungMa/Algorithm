import sys

a,b = map(int,sys.stdin.readline().rstrip().split(' '))

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))

numbers.reverse()

base = 1
real_number = 0
for i in numbers:
    real_number += base * i
    base *= a

base = 1
while(base < real_number):
    base *= b

base = base / b
result = []
while(base>=1):
    result.append(int(real_number//base))
    real_number = int(real_number%base)
    base = base / b

for i in result:
    print(i, end = " ")