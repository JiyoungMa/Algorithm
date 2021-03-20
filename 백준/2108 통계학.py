import sys

n = int(sys.stdin.readline().rstrip())

numbers = []
num_dict = dict()
for _ in range(n):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)
    if number not in num_dict.keys():
        num_dict[number] = 1
    else:
        num_dict[number] = num_dict[number] + 1

numbers.sort()


print(round(sum(numbers)/len(numbers)))
print(numbers[len(numbers)//2])

value = num_dict.values()
max_value = max(value)
v = [x for x in num_dict.keys() if num_dict[x] == max_value]
if len(v) > 1:
    v.sort()
    print(v[1])
else:
    print(v[0])

print(max(numbers) - min(numbers))

