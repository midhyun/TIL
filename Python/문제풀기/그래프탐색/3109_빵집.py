import sys
sys.stdin = open('3109_빵집.txt')
input = sys.stdin.readline

def BFS(start):
    i, j = start
    if j == M-1:
        return False
    for k in dir:
        y, x = i + k[0], j +k[1]
        if 0 <= y < N and 0 <= x < M and not visited[y][x] and graph[y][x] == '.':
            visited[y][x] = True
            if not BFS((y, x)):
                return
    return True

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dir = [(-1,1),(0,1),(1,1)]

for x in range(N):
    BFS((x, 0))

result = 0
for i in range(N):
    if visited[i][M-1]:
        result += 1

print(result)