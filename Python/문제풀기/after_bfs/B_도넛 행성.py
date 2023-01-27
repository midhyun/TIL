import sys
from collections import deque
sys.stdin = open('B_도넛 행성.txt')
input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [-1, 1, 0 , 0]
def bfs(i ,j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            y = (i + dy[k])%n
            x = (j + dx[k])%m
            if graph[y][x] == 0:
                graph[y][x] = 1
                q.append((y, x))


n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            bfs(i, j)
            result += 1
print(result)