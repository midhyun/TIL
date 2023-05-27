import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = sys.maxsize
matrix = [[] for _ in range(V+1)]
graph = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = INF
for i in range(1, V+1):
    result = min(result, graph[i][i])
if result == INF:
    print(-1)
else:
    print(result)