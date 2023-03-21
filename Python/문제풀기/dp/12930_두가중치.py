import sys
sys.stdin = open('12930_두가중치.txt')
input = sys.stdin.readline

# N개의 정점으로 이루어진 그래프의 간선은
# 가중치1, 가중치2 의 가중치를 2개 가지고있다.
# 0번 정점에서 1번 정점으로 가는 최단 경로를 찾는 > 다익스트라
# 경로의 비용은 sum(가중치1) * sum(가중치2)
def dijkstra(cur, cost, cost2):
    if dp[cur][cost] != -1:
        dp[cur][cost] = min(dp[cur][cost], cost2)
        return dp[cur][cost]
    else:
        dp[cur][cost] = cost2
    
    if cur == 1:
        return dp[cur][cost]
    
    for i in range(N):
        if graph1[cur][i]:
            nxt_cost = cost + graph1[cur][i] # 가중치1
            nxt_cost2 = dp[cur][cost] + graph2[cur][i] # 가중치2
            if nxt_cost < MAX and nxt_cost2 < MAX:
                dijkstra(i, nxt_cost, nxt_cost2)
    
    return dp[cur][cost]

N = int(input())
INF = sys.maxsize
MAX = N*10+1
graph1 = []
graph2 = []
for _ in range(N):
    graph1.append(list(map(lambda x: int(x) if x != '.' else 0, input().strip())))

for _ in range(N):
    graph2.append(list(map(lambda x: int(x) if x != '.' else 0, input().strip())))

dp = [[-1]*(MAX) for _ in range(N)]


dijkstra(0, 0, 0)
result = INF
for i in range(MAX):
    if dp[1][i] != -1:
        result = min(result, i*dp[1][i])

if result != INF:
    print(result)
else:
    print(-1)