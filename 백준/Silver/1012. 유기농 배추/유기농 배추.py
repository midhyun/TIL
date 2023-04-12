import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 2468_유기농배추

T = int(input())

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def dfs(i, j):
    matrix[i][j] = 0
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < M and 0 <= y < N:
            if matrix[y][x] == 1:
                matrix[y][x] = 0
                dfs(y, x)

    return

    


for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        j , i = map(int, input().split())
        matrix[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                dfs(i, j)
                cnt += 1

    print(cnt)