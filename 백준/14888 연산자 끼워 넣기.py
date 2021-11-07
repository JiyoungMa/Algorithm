import sys
from itertools import permutations

n = map(int,sys.stdin.readline().rstrip())

numbers = list(map(int,sys.stdin.readline().rstrip().split(' ')))
operator = list(map(int,sys.stdin.readline().rstrip().split(' ')))

operators = []
operators.extend(['+' for i in range(operator[0])])
operators.extend(['-' for i in range(operator[1])])
operators.extend(['*' for i in range(operator[2])])
operators.extend(['/' for i in range(operator[3])])

op_list = list(permutations(operators,len(operators)))

maximum = -1000000000
minimum = 1000000000

for op in op_list:
    result = numbers[0]
    for i in range(len(op)):
        if op[i] == '+':
            result += numbers[i+1]
        elif op[i] =='-':
            result -= numbers[i+1]
        elif op[i] == '*':
            result =  result * numbers[i+1]
        elif op[i] == '/':
            if result < 0:
                result = (result*(-1)) // numbers[i+1] *(-1)
            else:
                result = result//numbers[i+1]
    
    if result > maximum:
        maximum = result

    if result < minimum :
        minimum = result

print(maximum)
print(minimum)
