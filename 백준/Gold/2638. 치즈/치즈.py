from collections import deque

def bfs(graph):
    visited = [[0]*M for _ in range(N)]
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    result = []
    while q:
        i, j = q.popleft()
        for k in range(4):
            ny, nx = i + dy[k], j + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if not graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                elif graph[ny][nx]:
                    if visited[ny][nx]:
                        result.append((ny, nx))
                    visited[ny][nx] += 1

    return result

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
cnt = 0
while True:
    cheese = bfs(graph)
    if not cheese:
        break
    for i, j in cheese:
        graph[i][j] = 0
    cnt += 1

print(cnt)
