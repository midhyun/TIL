import sys
input = sys.stdin.readline

INF = int(sys.maxsize)
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dp = [[INF]*(M+1) for _ in range(N+1)]
    dp[1][0] = 0
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    
    # i번노드 까지 도달하는데 j만큼의 비용
    for j in range(M+1):
        for i in range(1, N+1):
            if dp[i][j] != INF:
                for nxt, c, d in graph[i]:
                    dist = dp[i][j] + d
                    cost = j + c

                    if cost <= M and dist < dp[nxt][cost]:
                        dp[nxt][cost] = dist
    
    result = min(dp[N])
    if result == INF:
        print('Poor KCM')
    else:
        print(result)