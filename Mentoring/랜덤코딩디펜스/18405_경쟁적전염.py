import sys
from collections import deque
sys.stdin = open('18405_경쟁적전염.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# que (time, y, x)
def bfs():
    data = []
    for i in range(N):
        for j in range(N):
            graph[i][j] = (0, graph[i][j])
            if graph[i][j][1]:
                data.append((graph[i][j], 0, i, j))
    data.sort()

    q = deque(data)

    while q:
        virus, t, i, j = q.popleft()
        if t >= S:
            break
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < N and 0 <= x < N and (graph[y][x][1] == 0):
                graph[y][x] = (t+1, graph[i][j][1])
                q.append((virus, t+1, y, x))
bfs()
print(graph[X-1][Y-1][1])