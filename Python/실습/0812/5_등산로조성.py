import sys
sys.stdin = open("_등산로조성.txt")
T = int(input())

def dfs(i, j, dist, isdig):
    global m_dist
    if dist > m_dist:
        m_dist = dist
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if 0 <= x < N and 0 <= y < N and visited[y][x] == False:
            if m_map[y][x] < m_map[i][j] :
                visited[y][x] = True
                dfs(y, x, dist+1, isdig)
                visited[y][x] = False
            elif m_map[y][x] >= m_map[i][j] and isdig == False:
                for dig in range(1, K+1):
                    m_map[y][x] -= dig
                    isdig = True
                    if m_map[y][x] < m_map[i][j]:
                        visited[y][x] = True
                        dfs(y, x, dist+1, isdig)
                        visited[y][x] = False
                    isdig = False
                    m_map[y][x] += dig

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    m_map = [list(map(int, input().split())) for _ in range(N)]
    max_height = max([max(m_map[i]) for i in range(N)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    m_dist = 0
    
    for i in range(N):
        for j in range(N):
            if m_map[i][j] == max_height:
                visited = [[False]*N for _ in range(N)]
                visited[i][j] = True
                dfs(i, j, 1, False)
    print(f'#{test_case} {m_dist}')