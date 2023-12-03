import sys
from heapq import heappop, heappush
sys.stdin = open('22870_산책(large).txt')
input = sys.stdin.readline

def Solution():
    INF = sys.maxsize
    N, M = map(int, input().split())
    node = [[] for _ in range(N+1)]
    for _ in range(M):
        i, j, dist = map(int, input().split())
        node[i].append((j, dist))
        node[j].append((i, dist))
    for i in range(N+1): node[i].sort()
    S, E = map(int, input().split())

    def Dijkstra(visited, start, goal):
        
        distance = [INF]*(N+1)
        distance[start] = 0
        q = []
        heappush(q, (0, start))
        while q:
            d, cur = heappop(q)
            if distance[cur] < d: continue

            if cur == goal:
                return distance

            for nxt, dist in node[cur]:
                if nxt in visited: continue

                ndist = d + dist
                if ndist < distance[nxt]:
                    distance[nxt] = ndist
                    heappush(q, (ndist, nxt))

    distance = Dijkstra(set(), E, S)
    firstCost = 0
    cursor = S
    visited = set()
    while cursor != E:
        for nxt, cost in node[cursor]:
            if firstCost + cost + distance[nxt] == distance[S]:
                firstCost += cost
                visited.add(nxt)
                cursor = nxt
                break
    visited.remove(E)
    distances = Dijkstra(visited, S, E)
    print(firstCost + distances[E])

Solution()
