import sys
from collections import deque
sys.stdin = open('1389_케빈베이컨.txt')
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                dist[i] = dist[cur] + 1
                                
n ,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

min_dist = 101
result = 0
for i in range(1,n+1):
    visited = [False] * (n+1)
    dist = [0] * (n+1)
    bfs(i)
    if sum(dist) < min_dist:
        min_dist = sum(dist)
        result = i

print(result)