import sys
sys.stdin = open('20002_사과나무.txt')
input = sys.stdin.readline

N = int(input())
graph =[[0]*(N+1)] + [[0] + [*map(int, input().split())] for _ in range(N)]
result = max(graph[1][1:])

for i in range(1, N+1):
    graph[0][i] += graph[0][i-1]
    graph[i][0] += graph[i-1][0]
    result = max(max(graph[i][1:]), result)

for i in range(1, N+1):
    for j in range(1, N+1):
        graph[i][j] += graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1]

for k in range(1, N+1):
    for i in range(k, N+1):
        for j in range(k, N+1):
            tmp = graph[i][j] - graph[i-k][j] - graph[i][j-k] + graph[i-k][j-k]
            result = max(result, tmp)

print(result)