import sys
input = sys.stdin.readline


while True:
    N, M = map(int, input().split())
    if not N:
        break
    graph =[[0]*(M+1)] + [[0] + [*map(int, input().split())] for _ in range(N)]
    result = 0
    for i in range(N+1):
        for j in range(M+1):
            if graph[i][j]:
                graph[i][j] = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) + 1
                result = max(result, graph[i][j])

    print(result)