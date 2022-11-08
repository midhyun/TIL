import sys
from collections import deque
sys.stdin = open('16948_데스나이트.txt')
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())


d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
def bfs(start, end):
    graph = [[-1]*n for _ in range(n)]
    graph[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    while q:
        i, j = q.popleft()
        if (i, j) == end:
            break
        for k in range(6):
            x = j + d[k][1]
            y = i + d[k][0]
            if 0 <= x < n and 0 <= y < n and graph[y][x] == -1:
                graph[y][x] = graph[i][j] + 1
                q.append((y, x))
    return graph

graph = bfs((r1, c1), (r2, c2))
print(graph[r2][c2])
