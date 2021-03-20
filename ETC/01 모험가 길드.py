import sys

people = list(map(int,sys.stdin.readline().rstrip().split(' ')))

people.sort()

count_group = 0
i = 0
while (i<len(people)):
    if i+people[i] < len(people):
        i += people[i]
        count_group += 1
    else:
        break

print(count_group)
