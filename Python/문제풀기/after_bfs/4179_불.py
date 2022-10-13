import sys
from collections import deque
sys.stdin = open('4179_불.txt')
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [[i for i in input().strip()] for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(jh, fire):
    q= deque()
    q.append(jh)
    for fir in fire:
        q.append(fir)
    while q:
        i, j = q.popleft()
        if (j == 0 or j == c-1 or i == 0 or i == r-1) and graph[i][j] != 'F':
            return graph[i][j] + 1
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < r and 0 <= x < c and graph[y][x] != 'F' and graph[y][x] != '#':
                if graph[i][j] == 'F':
                    graph[y][x] = 'F'
                    q.append((y, x))
                elif graph[y][x] == '.':
                    graph[y][x] = graph[i][j] + 1
                    q.append((y, x))
    return 'IMPOSSIBLE'
                    

fire = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            graph[i][j] = 0
            jh = (i, j)
        if graph[i][j] == 'F':
            fire.append((i, j))

print(bfs(jh, fire))