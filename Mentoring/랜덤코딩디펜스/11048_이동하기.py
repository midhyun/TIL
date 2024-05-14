import sys
sys.stdin = open('11048_이동하기.txt')
input = sys.stdin.readline

def solution_dfs():
    N, M = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dx, dy = [1, 0, 1], [0, 1, 1]

    stack = [(0, 0)]
    visited[0][0] = graph[0][0]
    while stack:
        y, x = stack.pop()
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[y][x] + graph[ny][nx] > visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + graph[ny][nx]
                    stack.append((ny, nx))

    print(visited[N-1][M-1])

def solution_dp():
    N, M = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(N)]
    dp = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if j == 0:
                dp[i][j] = graph[i][j] + dp[i-1][j]
            else:
                dp[i][j] = graph[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    print(dp[N-1][M-1])

solution_dp()