import sys

num_str = sys.stdin.readline().rstrip()

numbers = []

for i in range(len(num_str)):
    numbers.append(int(num_str[i]))

result = 0
i = 0
while(i<len(numbers)):
    if(numbers[i] == 0):
        i += 1
    elif (numbers[i] == 1):
        if(i+1 < len(numbers)):
            left = (result+1) * numbers[i+1]
            right = result * (1+numbers[i+1])
            if(left>right):
                result = left
            else:
                result = right

            i +=2
        else:
            result +=1
    else:
        if(result != 0):
            result = result * numbers[i]
            i +=1
        else:
            result += numbers[i]
            i+=1

print(result)