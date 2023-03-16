import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra():
    q = []
    dp = [[INF]*(max(costs)+1) for _ in range(N+1)]
    # 우선순위 큐에 (다음노드, 단위 비용, 총 비용) 값 삽입
    dp[1][costs[1]] = 0
    heappush(q, (1, costs[1], 0))
    while q:
        # dist : 현재 총 비용, cost : 단위 비용, cur : 현재 정점
        cur, cost, dist = heappop(q)
        # N번 노드에 도착했을경우 dist 리턴
        if cur == N: return dist
        # 방문한 적 있으면 continue
        if dp[cur][cost] < dist: continue

        # 현재위치에서 다음노드
        for nxt, nxt_dist in graph[cur]:
            nxt_cost = min(costs[nxt], cost)
            if dp[nxt][cost] > dist + cost * nxt_dist:
                dp[nxt][cost] = dist + cost * nxt_dist
                heappush(q, (nxt, min(cost, costs[nxt]), dist + cost * nxt_dist))

INF = sys.maxsize
N, M = map(int, input().split())
costs = [-1] + [*map(int, input().split())]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())