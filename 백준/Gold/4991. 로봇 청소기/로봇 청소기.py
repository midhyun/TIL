import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= x < m and 0 <= y < n and visited[y][x] == -1 and graph[y][x] != 'x' :
                visited[y][x] = visited[i][j] + 1
                q.append((y, x))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    graph = [[i for i in input().strip()] for _ in range(n)]

    s_pos = []
    pos = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                continue
            elif graph[i][j] == 'o':
                s_pos = [(i, j)]
            elif graph[i][j] == '*':
                pos.append((i, j))

    position = s_pos+pos
    leng = len(position)
    combies = permutations(range(1, leng), leng-1)
    dp = [[0]*leng for _ in range(leng)]
    flag = True
    for i in range(leng):
        visited = [[-1]*m for _ in range(n)]
        bfs(position[i])
        for j in range(leng):
            if visited[position[j][0]][position[j][1]] == -1:
                flag = False
            dp[i][j] = visited[position[j][0]][position[j][1]]

    if not flag:
        print(-1)
    else:
        result = []
        for combi in combies:
            temp = 0
            cnt = 0
            for i in range(leng-1):
                cnt += dp[temp][combi[i]]
                temp = combi[i]
            result.append(cnt)
        print(min(result))
