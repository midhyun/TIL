import sys
input = sys.stdin.readline

def solution():
    N, M = int(input()), int(input())
    INF = sys.maxsize
    cost = [[INF]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        start, end, pay = map(int, input().split())
        cost[start][end] = min(cost[start][end], pay)
    
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