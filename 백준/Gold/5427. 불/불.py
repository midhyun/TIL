import sys
from collections import deque
input = sys.stdin.readline

def bfs(pos, fire):
        q = deque(fire + pos)
        while q:
            i, j = q.popleft()
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if graph[i][j] == '@' and (not (0 <= y < N) or not (0 <= x < M)):
                    print(visited[i][j])
                    return
                if 0 <= y < N and 0 <= x < M and not visited[y][x]:
                    if graph[y][x] == '.':
                        visited[y][x] = visited[i][j] + 1
                        graph[y][x] = graph[i][j]
                        q.append((y, x))
        print('IMPOSSIBLE')

T = int(input())
dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
for _ in range(T):
    M, N = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    pos = []
    fire = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '@':
                pos = [(i, j)]
                visited[i][j] = 1
            if graph[i][j] == '*':
                fire.append((i, j))
                visited[i][j] = 1

    
    bfs(pos, fire)