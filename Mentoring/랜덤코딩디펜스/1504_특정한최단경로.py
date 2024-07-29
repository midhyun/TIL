import sys
from heapq import heappush, heappop
sys.stdin = open('1504_특정한최단경로.txt')
input = sys.stdin.readline

def solution():
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]    
    for _ in range(E):
        a, b, cost = map(int, input().split())
        graph[a].append((cost, b))
        graph[b].append((cost, a))
    v1, v2 = map(int, input().split())
    
    
    def dijkstra(start):
        INF = sys.maxsize
        distance = [INF]*(N+1)
        distance[start] = 0
        heap = []
        heappush(heap, (0, start))
        while heap:
            curCost, cur = heappop(heap)
            for nxtCost, nxt in graph[cur]:
                dist = curCost + nxtCost
                if dist < distance[nxt]:
                    distance[nxt] = dist
                    heappush(heap, (dist, nxt))
        return distance
    dist_s = dijkstra(1)
    dist_v1 = dijkstra(v1)
    dist_v2 = dijkstra(v2)

    result = min(dist_s[v1] + dist_v1[v2] + dist_v2[N], dist_s[v2] + dist_v2[v1] + dist_v1[N])
    print(result if result < sys.maxsize else -1)

    return

solution()
