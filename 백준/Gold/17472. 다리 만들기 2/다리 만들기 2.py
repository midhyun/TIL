import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    visited = [[False] * M for _ in range(N)]

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b: parent[b] = a
        else: parent[a] = b

    def dfs(y, x, cnt):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = cnt
                dfs(ny, nx, cnt)

    def cnt_island():
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1 and not visited[i][j]:
                    cnt += 1
                    visited[i][j] = cnt
                    dfs(i, j, cnt)
        return cnt
    
    def make_bridge(y, x):
        bridge = []
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            cnt = 0
            while True:
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx]:
                        cnt += 1
                        ny += dy[k]
                        nx += dx[k]
                    elif visited[y][x] != visited[ny][nx] and cnt > 1:
                        bridge.append((cnt, visited[y][x], visited[ny][nx]))
                        break
                    else:
                        break
                else:
                    break
        return bridge
    # 섬의 개수 정의, visited 초기화
    islandCnt = cnt_island()
    edges = []
    parent = [ i for i in range(islandCnt+1)]
    # 설치가 가능한 다리 edge에 추가
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                bridges = make_bridge(i, j)
                for bridge in bridges:
                    edges.append(bridge)
    # 크루스칼 알고리즘
    edges.sort()
    result = 0
    edge_cnt = 0
    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
            edge_cnt += 1
    if edge_cnt == islandCnt-1:
        print(result)
    else:
        print(-1)
    return

solution()
