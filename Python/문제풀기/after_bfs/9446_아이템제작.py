import sys
from heapq import heappop, heappush
sys.stdin = open('9446_아이템제작.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
prices = [0]+[*map(int, input().split())]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, x, y = map(int, input().split())
    graph[x].append((a, y))
    graph[y].append((a, x))

q = []
for i, price in enumerate(prices):
    heappush(q, (price, i))

while q:
    price, i = heappop(q)
    if price > prices[i]:
        continue
    for dx, x in graph[i]:
        nx = price + prices[x]
        if prices[dx] > nx:
            prices[dx] = nx
            heappush(q, (nx, dx))
print(prices[1])