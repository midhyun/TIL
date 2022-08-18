import sys
sys.stdin = open('2468_안전영역.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#2468_안전영역
# 지역의 높이
# 물에 잠기지 않는 안전한 영역의 최대 개수

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i, j):
    visited[i][j] = True
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < N and 0 <= y < N :
            if matrix[y][x] > h and not visited[y][x]:
                visited[y][x] = True
                bfs(y, x)
cnt_lst = [] 
for h in range(101):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > h and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    cnt_lst.append(cnt)
print(max(cnt_lst))