import sys
from collections import deque
sys.stdin = open('14503_로봇청소기.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
now = [*map(int, input().split())]
graph = [[*map(int, input().split())] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
d = [(-1,0),(0,1),(1,0),(0,-1)]
q = deque()
q.append((now[0], now[1]))
visited[now[0]][now[1]] = 1
while q:
    i, j = q.popleft()
    for k in range(1, 5):
        dir = (now[2]-k)%4
        y = i + d[dir][0]
        x = j + d[dir][1]
        if 0 <= y < N and 0 <= x < M and not graph[y][x] and not visited[y][x]:
            visited[y][x] = 1
            q.append((y, x))
            now = [y, x, dir]
            break
    else:
        dir = (now[2]-2)%4
        if graph[i+d[dir][0]][j+d[dir][1]]:
            break
        else:
            q.append((i+d[dir][0], j+d[dir][1]))
            now[0], now[1] = i+d[dir][0], j+d[dir][1]

result = 0            
for visit in visited:
    result += sum(visit)
print(result)