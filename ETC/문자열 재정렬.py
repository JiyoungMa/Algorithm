import sys

input_list = list(sys.stdin.readline().rstrip())
alpha = []
number = 0

for i in input_list:
    if i>='0' and i<='9':
        number += int(i)
    else:
        alpha.append(i)

alpha.sort()
alpha = "".join(alpha)
print(alpha+str(number))