import sys
from collections import deque
sys.stdin = open('14940_쉬운 최단거리.txt')
input = sys.stdin.readline

def solution():
    def find():
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2:
                    start = (i, j)
                    visited[i][j] = 0
                elif graph[i][j] == 0:
                    visited[i][j] = 0
        return start

    N, M = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append(find())

    while q:
        i, j = q.popleft()
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < N and 0 <= x < M and visited[y][x] == -1 and graph[y][x] == 1:
                visited[y][x] = visited[i][j] + 1
                q.append((y, x))
    
    for v in visited:
        print(*v)
solution()