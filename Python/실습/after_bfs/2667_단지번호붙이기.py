import sys
sys.stdin = open('2667_단지번호붙이기.txt')
input = sys.stdin.readline

N = int(input())

matrix = [[int(i) for i in list(input().strip())] for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(visited, i, j):
    global cnt
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < N and 0 <= y < N:
            if not visited[y][x] and matrix[y][x] == 1:
                visited[y][x] = True
                cnt += 1
                dfs(visited, y, x)

cnt_complex = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j]:
            visited[i][j] = True
            cnt = 1
            dfs(visited, i, j)
            cnt_complex.append(cnt)

print(len(cnt_complex), *sorted(cnt_complex), sep= '\n')
