import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[[[False] * M for i in range(N)] for i in range(M)] for i in range(N)]
r = (); b = (); o = ()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            r = (i, j)
        elif graph[i][j] == 'B':
            b = (i, j)
        elif graph[i][j] == 'O':
            o = (i, j)

def move(i, j, dy, dx):
    cnt = 0
    while graph[i + dy][j + dx] != "#" and graph[i][j] != "O":
        i += dy
        j += dx
        cnt += 1
    return i, j, cnt

def bfs(ri, rj, bi, bj, cur):
    q = deque()
    q.append((ri, rj, bi, bj, cur))
    visited[ri][rj][bi][bj] = True
    while q:
        ri, rj, bi, bj, cur = q.popleft()
        if cur > 10:
            break
    
        for k in range(4):
            nri, nrj, rc = move(ri, rj, dy[k], dx[k])
            nbi, nbj, bc = move(bi, bj, dy[k], dx[k])
            if graph[nbi][nbj] != "O":
                if graph[nri][nrj] == "O":
                    print(1)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc:
                        nri -= dy[k]
                        nrj -= dx[k]
                    else:
                        nbi -= dy[k]
                        nbj -= dx[k]
                if not visited[nri][nrj][nbi][nbj]:
                    visited[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, cur + 1])
    print(0)

bfs(r[0], r[1], b[0], b[1], 1)