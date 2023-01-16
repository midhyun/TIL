import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = []
for _ in range(n):
    m, v = map(int, input().split())
    jewelry.append((m, v))
heapq.heapify(jewelry)
bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()
result = 0
temp = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewelry)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not jewelry:
        break
print(result)