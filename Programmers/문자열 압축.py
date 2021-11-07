import sys

input_str = sys.stdin.readline().rstrip()
minimum = len(input_str)

for length in range(1,len(input_str)//2+1,1):
    cut = [input_str[i:i+length] for i in range(0, len(input_str), length)]
    now_str = ''
    now_count = 1
    result = ''

    for s in cut:
        if s != now_str and now_count != 1:
            result += str(now_count) + now_str
            now_str = s
            now_count = 1
        elif s != now_str and now_count == 1:
            result += now_str
            now_str = s
            now_count = 1
        else:
            now_count += 1
    
    if now_count != 1:
        result += str(now_count) + now_str
    else:
        result += now_str

    if minimum > len(result):
        minimum = len(result)

print(minimum)
