import sys
input = sys.stdin.readline

def solution():
    INF = sys.maxsize
    N, K = map(int, input().split())
    distance = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                distance[i][j] = 0

    for _ in range(K):
        a, b = map(int, input().split())
        distance[a][b] = 1
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    S = int(input())
    for _ in range(S):
        pre, post = map(int, input().split())
        if distance[pre][post] < INF:
            print(-1)
        elif distance[post][pre] < INF:
            print(1)
        else:
            print(0)

solution()
