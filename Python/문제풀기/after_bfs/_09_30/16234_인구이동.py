import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, l, r = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]
def bfs(p):
    temp = graph[p[0]][p[1]]
    countries = [(p[0], p[1])]
    q = deque()
    q.append(p)
    visited[p[0]][p[1]] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < n and 0 <= y < n:
                diff = abs(graph[i][j] - graph[y][x])
                if not visited[y][x] and l <= diff <= r:
                    visited[y][x] = True
                    q.append((y, x))
                    countries.append((y, x))
                    temp += graph[y][x]

    return temp, countries

cnt = 0
while True:
    flag = False
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tem, countries = bfs((i,j))
                num = len(countries)
                people = tem//num
                if num == 1:
                    continue
                for country in countries:
                    graph[country[0]][country[1]] = people
                flag = True
    if flag:
        cnt += 1
    else: break
print(cnt)