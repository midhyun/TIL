import sys
from collections import deque
sys.stdin = open('2638_치즈.txt')
input = sys.stdin.readline

def find_melt(graph, cheese):
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    melt_result = []
    cheese_result = []
    while cheese:
        i, j = cheese.pop()
        outside = 0
        for k in range(4):
            if not graph[i+dy[k]][j+dx[k]]:
                outside += 1
        if outside >= 2:
            melt_result.append((i, j))
        else:
            cheese_result.append((i, j))

    return melt_result, cheese_result

def melting(graph, melt):
    for i, j in melt:
        graph[i][j] = 0

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cheese = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cheese.append((i, j))

result = 0
while cheese:
    melt, cheese = find_melt(graph, cheese)
    melting(graph, melt)

    result += 1

print(result)