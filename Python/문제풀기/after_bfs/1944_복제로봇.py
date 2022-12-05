import sys
from heapq import heappush, heappop
from collections import deque
sys.stdin = open('1944_복제로봇.txt')
input = sys.stdin.readline
dx, dy = [0,0,-1,1], [-1,1,0,0]
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

cnt = 0
points = []
S = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            points.append((i, j))
            graph[i][j] = cnt
            S = cnt
            cnt += 1
        if graph[i][j] == 'K':
            points.append((i, j))
            graph[i][j] = cnt
            cnt += 1

def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 0
    temp = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            y, x = i + dy[k], j + dx[k]
            if 0 <= y < n and 0 <= x < n and visited[y][x] == -1 and graph[y][x] != '1':
                visited[y][x] = visited[i][j] + 1
                if isinstance(graph[y][x],int):
                    temp += 1
                    q.append((y, x))
                    edges.append((graph[start[0]][start[1]], graph[y][x], visited[y][x]))
                else:
                    q.append((y,x))
    if temp != m:
        return False
    return True

edges = []
flag = True
for point in points:
    visited = [[-1]*n for _ in range(n)]
    if not bfs(point):
        flag = False
        break
if not flag:
    print(-1)
else:
    nodes = [[] for _ in range(m+1)]
    for a, b, dist in edges:
        nodes[a].append((dist, b))

    visited = [False] * (m+1)
    start = []
    heappush(start, [0, S])
    result, cnt = 0, 0
    while start:
        x, node = heappop(start)
        if cnt == m+1:
            break
        if not visited[node]:
            visited[node] = True
            cnt += 1
            result += x
            for k, v in nodes[node]:
                heappush(start, [k, v])
    print(result)