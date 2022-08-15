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
        if 0 <= x < N and 0 <= y < N and not visited[y][x]:
            if m_map[y][x] < m_map[i][j]:
                visited[y][x] = True
                dfs(y, x, dist+1, isdig)
                visited[y][x] = False
            elif m_map[y][x] >= m_map[i][j] and not isdig:
                for dig in range(1, K+1):                       # 1부터 K만큼의 깊이를 한칸씩 낮춥니다.
                    m_map[y][x] -= dig
                    isdig = True                                # 땅을 한번만 팔 수 있기 때문에 불리언으로 표시
                    if m_map[y][x] < m_map[i][j]:               # 땅을 팠는데 현재 위치보다 낮아질 때, 방문가능 방문 표시 하면서 거리를 +1
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