import sys
import heapq
sys.stdin = open('1504_특정한최단경로.txt')
input = sys.stdin.readline

INF = 1e9
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

s_dp = dijkstra(1)
v_dp = dijkstra(v)
u_dp = dijkstra(u)

cnt = min(s_dp[v] + v_dp[u] + u_dp[N], s_dp[u]+ u_dp[v] + v_dp[N])
print(cnt if cnt < INF else -1)