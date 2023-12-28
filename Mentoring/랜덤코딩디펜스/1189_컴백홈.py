import sys
sys.stdin = open('1189_컴백홈.txt')
input = sys.stdin.readline

def solution():
    R, C, K = map(int, input().split())
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    graph = [list(input().rstrip()) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    visited[R-1][0] = True
    result = 0

    def dfs(i, j, cur):
        # 지역변수를 사용하기 위한 nonlocal 키워드.
        # 가장 가까운 함수부터 지역변수를 찾는다.
        nonlocal result
        if i == 0 and j == C-1 and cur == K:
            result += 1
            return
        
        if cur > K:
            return

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < R and 0 <= x < C and not visited[y][x] and graph[y][x] != 'T':
                visited[y][x] = True
                dfs(y, x, cur+1)
                visited[y][x] = False
    
    dfs(R-1, 0, 1)
    print(result)

solution()
