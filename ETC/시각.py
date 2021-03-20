import sys

n = int(sys.stdin.readline().rstrip())

yes_three = n//3
no_three = n+1-yes_three

print(yes_three*3600 + no_three*1575)