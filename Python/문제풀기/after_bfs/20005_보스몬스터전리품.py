import sys
from collections import deque
sys.stdin = open('20005_보스몬스터전리품.txt')
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m, p = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
users = {}
users_t = []
for _ in range(p):
    id, dps = input().split()
    dps = int(dps)
    users[id] = users.get(id, dps)
boss = int(input())
user = []
for i in range(n):
    for j in range(m):
        if not (graph[i][j] == '.') and not (graph[i][j] == 'X') and not(graph[i][j] == 'B'):
            user.append((graph[i][j], i, j))
def bfs(start):
    q = deque()
    q.append((start[0],start[1], 0))
    while q:
        i, j, t = q.popleft()
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < n and 0 <= x < m and not visited[y][x] and not graph[y][x] == 'X':
                if graph[y][x] == 'B':
                    return t+1
                visited[y][x] = True
                q.append((y,x,t+1))
    return 1000000
for u in user:
    visited = [[0]*m for _ in range(n)]
    temp = bfs((u[1], u[2]))
    if temp:
        users_t.append((temp, u[0]))

users_t.sort()
q = deque(users_t)
now_dps = 0
now_t = 0
while boss > 0:
    while True:
        if q and q[0][0] == now_t:
            a = q.popleft()
            now_dps += users[a[1]]
        else:
            break
    boss -= now_dps
    now_t += 1
print(p-len(q))