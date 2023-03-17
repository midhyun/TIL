import sys
from heapq import heappop, heappush
sys.stdin = open('13308_주유소.txt')
input = sys.stdin.readline
# 음의간선이 없고 간선의 가중치가 있을 경우, 다익스트라
# BFS를 수행하는데 큐대신 우선순위 큐를 활용함.
def dijkstra():
    INF = sys.maxsize
    # dp[i][j] : i번도시까지, 단위비용j 일때 최소비용
    dp = [[INF]*(max(costs)+1) for _ in range(N+1)]
    q = []
    dp[1][costs[1]] = 0
    # !! 힙자료구조 사용시 튜플의 첫번째 요소기준에 주의. !!
    heappush(q, (0, costs[1], 1))
    while q:
        # dist : 총 비용, cost : 단위비용, cur : 현재위치
        dist, cost, cur = heappop(q)
        # 도착지까지의 총 비용 리턴
        if cur == N:
            return dist
        # 이미 더 작은 총 비용일 경우 continue
        if dp[cur][cost] < dist:
            continue
        # 현재 정점에서 bfs 수행
        for next, next_dist in graph[cur]:
            next_cost = min(costs[next], cost)
            # 다음정점까지의 기존 비용보다, 현재정점을 거쳐서가는 비용이 더 적을때
            if dp[next][cost] > dist + cost * next_dist:
                dp[next][cost] = dist + cost * next_dist
                heappush(q, (dist + cost * next_dist, next_cost, next))

N, M = map(int, input().split())
costs = [-1] + [*map(int, input().split())]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())