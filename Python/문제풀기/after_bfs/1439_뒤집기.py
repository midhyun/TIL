import sys
sys.stdin= open('1439_뒤집기.txt')
input = sys.stdin.readline

s = input().strip()
temp = s[0]
a = 0
b = 0
if temp == '1':
    a += 1
else:
    b += 1

for i in range(1, len(s)):
    if temp == s[i]:
        continue
    if s[i] == '1':
        a += 1
    else:
        b += 1
    temp = s[i]

print(min(a, b))