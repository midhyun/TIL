import sys
from collections import deque
sys.stdin = open('16197_두동전.txt')
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
graph = [[i for i in input().strip()] for _ in range(n)]
visited  = [[[-1]*2 for _ in range(m)] for _ in range(n)]

def bfs(a,b,c,d):
    q = deque()
    q.append((a,b,c,d))
    visited[a][b][0], visited[c][d][1] = 0, 0
    while q:
        i1, j1, i2, j2  = q.popleft()
        for k in range(4):
            y1, x1 = i1 + dy[k], j1 + dx[k] 
            y2, x2 = i2 + dy[k], j2 + dx[k]
            if visited[a][b][0] > 10:
                print(-1)
                exit(0)
            elif (0 <= y1 < n and 0 <= x1 < m) and (0 <= y2 < n and 0 <= x2 < m):
                if graph[y1][x1] != '#':
                    visited[y1][x1][0] = visited[i1][j1][0] + 1
                else:
                    visited[i1][j1][0] += 1
                    y1, x1 = i1, j1
                if graph[y2][x2] != '#':
                    visited[y2][x2][1] = visited[i2][j2][0] + 1
                else:
                    visited[i2][j2][0] += 1
                    y2, x2 = i2, j2
                q.append((y1,x1,y2,x2))
            elif (0 <= y1 < n and 0 <= x1 < m) or (0 <= y2 < n and 0 <= x2 < m):
                print(y1,x1,y2,x2)
                print(visited[i1][j1][0]+1)
                break
        for visit in visited:
            print(visit)
        print('------------------')
            

start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            start.append(i)
            start.append(j)

bfs(*start)
