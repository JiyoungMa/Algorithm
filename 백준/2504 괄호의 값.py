import sys

input_list = list(sys.stdin.readline().rstrip())

left = []
right = []

result = 0
l_count = 0
r_count = 0

result_list = []
for i in input_list:
    if i == '(' or i == '[':
        left.append(i)
        l_count += 1
    else:
        right.append(i)
        r_count += 1

    if l_count<r_count:
        print(0)
        break

    if i == ')':
        mr = 0
        l = left.pop()
        r = right.pop()
        while (l != '('):
            if type(l) != int:
                print(0)
                sys.exit()
            mr += l
            l = left.pop()
        
        if mr == 0:
            mr = 1
        mr *= 2
        left.append(mr)
    
    elif i == ']':
        mr = 0
        l = left.pop()
        r = right.pop()
        while (l != '['):
            if type(l) != int:
                print(0)
                sys.exit()
            mr += l
            l = left.pop()
        
        if mr == 0:
            mr = 1
        mr *= 3
        left.append(mr)

if l_count != r_count:
    print(0)
    sys.exit()

print(sum(left))