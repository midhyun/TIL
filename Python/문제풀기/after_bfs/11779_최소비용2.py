import sys
from heapq import heappop, heappush
sys.stdin = open('11779_최소비용2.txt')
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

A, B = map(int, input().split())
path = [[] for _ in range(n+1)]
q = []
heappush(q, (0, A))
visited[A] = 0
path[A] = [A]
while q:
    dist, node = heappop(q)
    if dist > visited[node]:
        continue
    for nd, x in graph[node]:
        cost = dist + nd
        if visited[x] > cost:
            visited[x] = cost
            path[x] = path[node] + [x]
            heappush(q, (cost, x))

print(visited[B])
print(len(path[B]))
print(*path[B])