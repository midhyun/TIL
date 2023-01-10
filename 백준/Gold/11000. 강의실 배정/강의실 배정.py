import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a ,b = map(int, input().split())
    lst.append((a, b))
lst.sort()
room = []
heappush(room, lst[0][1])

for i in range(1, n):
    if lst[i][0] >= room[0]:
        heappop(room)
    heappush(room, lst[i][1])

print(len(room))