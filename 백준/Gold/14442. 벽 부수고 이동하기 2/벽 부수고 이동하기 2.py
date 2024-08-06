import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    def bfs():
        queue = deque([(0, 0, K)])
        visited[0][0][K] = 1

        while queue:
            y, x, breakable = queue.popleft()
            
            if y == N-1 and x == M-1:
                return visited[y][x][breakable]
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= ny < N and 0 <= nx < M:
                    if graph[ny][nx] == 1 and breakable and not visited[ny][nx][breakable-1]:
                        visited[ny][nx][breakable-1] = visited[y][x][breakable] + 1
                        queue.append((ny, nx, breakable-1))
                    elif graph[ny][nx] == 0 and not visited[ny][nx][breakable]:
                        visited[ny][nx][breakable] = visited[y][x][breakable] + 1
                        queue.append((ny, nx, breakable))

        return -1
    
    print(bfs())

solution()
