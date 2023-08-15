import sys
sys.stdin = open('/Users/hj/midhyun/TIL/Mentoring/랜덤코딩디펜스/11123_양한마리양두마리.txt')
input = sys.stdin.readline

def DFS(y, x):
    stack = [(y, x)]
    visited[y][x] = True

    while stack:
        y, x = stack.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == '#' and not visited[ny][nx]:
                    stack.append((ny, nx))
                    visited[ny][nx] = True

    return 1

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '#' and not visited[i][j]:
                cnt += DFS(i, j)
    
    print(cnt)