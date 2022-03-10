import sys

strs = sys.stdin.readline().rstrip()

maximum = ""
minimum = ""

string_split = strs.split("K")

for s in range(len(string_split)-1):
    now_str = string_split[s]
    if len(now_str) == 0:
        maximum += str(5)
        minimum += str(5)
    else:
        mcount = len(string_split[s])
        maximum += str(5*10**mcount)
        minimum += str(10**(mcount-1)) + str(5)

now_str = string_split[-1]
if len(now_str) != 0 : 
    mcount = len(now_str)
    now_list = ["1"]*len(now_str)
    maximum += ''.join(now_list)
    minimum += str(10**(len(now_str)-1))

print(maximum)
print(minimum)
