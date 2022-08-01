import sys
input = sys.stdin.readline

line = input().strip().split('-')
result = ''
for word in line:
    result += word[0]

print(result)