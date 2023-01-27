import sys
from collections import deque
sys.stdin = open('1744_수 묶기.txt')
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
q = deque(nums)
result = 0
while q:
    x = q.popleft()
    if x < 0 and q:
        y = q.popleft()
        if y < 0:
            result += x*y
        elif y == 0:
            continue
        else:
            q.appendleft(y)
            result += x
    elif x == 0:
        continue
    elif x == 1:
        result += x
    elif x > 0 and q and len(q)%2 == 1:
        y = q.popleft()
        result += x*y
    else:
        result += x

print(result)