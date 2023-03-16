import sys
from heapq import heappop, heappush
sys.stdin = open('13308_주유소.txt')
input = sys.stdin.readline

def dijkstra():
    INF = sys.maxsize
    # dp[i][j] : i번도시까지, 단위비용j 일때 최소비용
    dp = [[INF]*(max(costs)+1) for _ in range(N+1)]
    q = []
    dp[1][costs[1]] = 0
    heappush(q, (0, costs[1], 1))
    while q:
        # now_dist : 총 비용, now_cost : 단위비용, now : 현재위치
        now_dist, now_cost, now = heappop(q)
        if now == N:
            return now_dist
        if dp[now][now_cost] < now_dist:
            continue
        for next, next_dist in graph[now]:
            next_cost = min(costs[next], now_cost)
            if dp[next][now_cost] > now_dist + now_cost * next_dist:
                dp[next][now_cost] = now_dist + now_cost * next_dist
                heappush(q, (now_dist + now_cost * next_dist, next_cost, next))

N, M = map(int, input().split())
costs = [-1] + [*map(int, input().split())]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())