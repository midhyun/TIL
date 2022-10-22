import sys
from collections import deque
sys.stdin = open('16954_움직이는미로탈출.txt')
input = sys.stdin.readline

dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
graph = [list(input().strip()) for _ in range(8)]

graph[7][0] = 0
q_now = deque([(7,0)])
q_nxt = deque()

while q_now or q_nxt:
    if graph[0][7] != '.':
        break
    visited = [[False]*8 for _ in range(8)]
    while q_now:
        i, j = q_now.popleft()
        if graph[i][j] == '#':
            continue
        q_nxt.append((i, j))
        for k in range(8):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < 8 and 0 <= y < 8 and not visited[y][x] and graph[y][x] != '#':
                graph[y][x] = graph[i][j] + 1
                visited[y][x] = True
                q_nxt.append((y, x))
    q_nxt, q_now = q_now, q_nxt

    for i in range(7,-1,-1):
        for j in range(8):
            if i == 7:
                if graph[i][j] == '#':
                    graph[i][j] = '.'
            else:
                if graph[i][j] == '#':
                    graph[i][j] = '.'
                    graph[i+1][j] = '#'
if graph[0][7] == '.':
    print(0)
else:
    print(1)