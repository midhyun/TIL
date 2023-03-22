import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# N개의 정점으로 이루어진 그래프의 간선은
# 가중치1, 가중치2 의 가중치를 2개 가지고있다.
# 0번 정점에서 1번 정점으로 가는 최단 경로를 찾는 > 다익스트라
# 경로의 비용은 sum(가중치1) * sum(가중치2)

N = int(input())
INF = sys.maxsize
MAX = N*10+1
graph1 = []
graph2 = []
for _ in range(N):
    graph1.append(list(map(lambda x: int(x) if x != '.' else 0, input().strip())))
for _ in range(N):
    graph2.append(list(map(lambda x: int(x) if x != '.' else 0, input().strip())))
dp = [[INF]*(MAX) for _ in range(N)]
dp[0][0] = 0

q = []
heappush(q, (0, 0, 0))
while q:
    cost1, cur, cost2 = heappop(q)

    if dp[cur][cost1] < cost2:
        continue

    for nxt in range(N):
        nxt_cost1 = graph1[cur][nxt]
        nxt_cost2 = graph2[cur][nxt]

        if nxt_cost1 == 0:
            continue

        nxt_cost1 += cost1
        nxt_cost2 += cost2

        if nxt_cost1 >= MAX or dp[nxt][nxt_cost1] <= nxt_cost2:
            continue

        dp[nxt][nxt_cost1] = nxt_cost2
        heappush(q, (nxt_cost1, nxt, nxt_cost2))
        
result = INF

for i in range(MAX):
    if dp[1][i] < result:
        result = min(result, dp[1][i] * i)

if result != INF:
    print(result)
else:
    print(-1)