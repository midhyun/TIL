import sys
from collections import deque
sys.stdin = open('2583_영역구하기.txt')
input = sys.stdin.readline

n ,m, k = map(int, input().split())
graph = [[0]*(m) for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(start):
    cnt = 1
    q = deque()
    q. append(start)
    graph[start[0]][start[1]] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < m and 0 <= y < n:
                if graph[y][x] == 0:
                    graph[y][x] = 1
                    q.append((y, x))
                    cnt += 1
    return cnt
result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result.append(bfs((i, j)))

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')