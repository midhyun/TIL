import sys
sys.stdin = open('10217_KCMTravel.txt')
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
        # 출발지인 1번노드부터, BFS탐색진행
        for i in range(1, N+1):
            if dp[i][j] != INF:
                # 다음노드, 비용, 시간
                for nxt, c, d in graph[i]:
                    dist = dp[i][j] + d
                    cost = j + c

                    if cost <= M and dist < dp[nxt][cost]:
                        dp[nxt][cost] = dist
    
    for i in range(N+1):
        for j in range(M+1):
            if dp[i][j] == INF:
                dp[i][j] = -1
    
    for d in dp:
        print(d)

    result = min(dp[N])
    if result == INF:
        print('Poor KCM')
    else:
        print(result)