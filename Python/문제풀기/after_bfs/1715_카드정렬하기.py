import sys
from heapq import heappop, heappush
sys.stdin = open('1715_카드정렬하기.txt')
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heappush(q, int(input()))
result = 0
if n == 1:
    print(0)
    exit()

for _ in range(n-1):
    temp = heappop(q) + heappop(q)
    result += temp
    heappush(q, temp)
print(result)