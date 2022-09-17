import sys
sys.stdin = open('13460_구슬탈출2.txt')
from collections import deque
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def move(i, j, di, dj):
    c = 0
    while s[i + di][j + dj] != "#" and s[i][j] != "O":
        i += di
        j += dj
        c += 1
    return i, j, c
    
def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            rni, rnj, rc = move(ri, rj, dx[i], dy[i])
            bni, bnj, bc = move(bi, bj, dx[i], dy[i])
            if s[bni][bnj] != "O":
                if s[rni][rnj] == "O":
                    print(d)
                    return
                if rni == bni and rnj == bnj:
                    if rc > bc:
                        rni -= dx[i]
                        rnj -= dy[i]
                    else:
                        bni -= dx[i]
                        bnj -= dy[i]
                if not visit[rni][rnj][bni][bnj]:
                    visit[rni][rnj][bni][bnj] = True
                    q.append([rni, rnj, bni, bnj, d + 1])
    print(-1)

visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
s = []
for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j

q = deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
bfs()