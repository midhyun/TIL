import sys
from heapq import heappop, heappush
input = sys.stdin.readline

INF = sys.maxsize
N, M = map(int, input().split())
costs = [0] + [*map(int, input().split())]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dp = [[INF]*(max(costs)+1) for _ in range(N+1)]

def dijkstra():
    q = []
    # 우선순위 큐에 (다음노드, 단위 비용, 총 비용) 값 삽입
    heappush(q, (1, costs[1], 0))
    while q:
        cur, cost, dist = heappop(q)
        # N번 노드에 도착했을경우 dist 리턴
        if cur == N: return dist
        # 방문한 적 있으면 continue
        if dp[cur][cost] < dist: continue

        # 현재위치에서 다음노드
        for nxt, nxt_dist in graph[cur]:
            tmp = dist + cost * nxt_dist
            if dp[nxt][cost] > tmp:
                dp[nxt][cost] = tmp
                heappush(q, (nxt, min(cost, costs[nxt]), tmp))

print(dijkstra())