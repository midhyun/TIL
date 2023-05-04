import sys
sys.stdin = open('18430_무기공학.txt')
input = sys.stdin. readline

def dfs(i, j, total):
    global result

    if j == M:
        i += 1
        j = 0
    
    if i == N:
        result = max(result, total)
        return
    
    if not visited[i][j]:
        for k in range(4):
            y1 = i + shape[k][0]
            x1 = j + shape[k][1]
            y2 = i + shape[k][2]
            x2 = j + shape[k][3]
            if 0 <= y1 < N and 0 <= x1 < M and 0 <= y2 < N and 0 <= x2 < M:
                if not visited[y1][x1] and not visited[y2][x2]:
                    visited[i][j] = True
                    visited[y1][x1] = True
                    visited[y2][x2] = True
                    hard = (matrix[i][j]*2) + matrix[y1][x1] + matrix[y2][x2]
                    dfs(i, j+1, total+hard)
                    visited[i][j] = False
                    visited[y1][x1] = False
                    visited[y2][x2] = False

    dfs(i, j+1, total)
    return

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
shape = [[0, -1, 1, 0], [0, -1, -1, 0], [-1, 0, 0, 1], [1, 0, 0, 1]]

result = 0
dfs(0, 0, 0)

print(result)