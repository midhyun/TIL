import sys
sys.stdin = open('11404_플로이드.txt')
input = sys.stdin.readline

def solution():
    N, M = int(input()), int(input())
    INF = sys.maxsize
    cost = [[INF]*(N+1) for _ in range(N+1)]
    # 비용 초기화
    for _ in range(M):
        start, end, pay = map(int, input().split())
        cost[start][end] = min(cost[start][end], pay)
    # 플로이드 워셜, dp: i -> j 와 i -> k -> j 중 최소값 선택
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    cost[i][j] = 0
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    for c in cost[1:]:
        c = list(map(lambda x: 0 if x == INF else x, c[1:]))
        print(*c)

solution()
