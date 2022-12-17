import sys
sys.stdin = open('1938_통나무옮기기.txt')
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[[-1,-1] for _ in range(n)] for _ in range(n)]
start = []
end = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'B':
            start.append([i, j])
        elif graph[i][j] == 'E':
            end.append((i, j))

