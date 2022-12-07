import sys
from heapq import heappop, heappush
sys.stdin = open('20128_Parity.txt')
input = sys.stdin.readline

INF = int(sys.maxsize)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((dist, b))
    graph[b].append((dist, a))

distance = [[INF]*2 for _ in range(n+1)]
distance[1][0] = 0
q = []
heappush(q, (0, 1))
while q:
    dist, cur = heappop(q)
    if distance[cur][1] < dist and dist%2:
        continue
    elif distance[cur][0] < dist and not dist%2:
        continue
    for i in graph[cur]:
        cost = dist + i[0]
        if cost%2: #홀수이면
            if cost < distance[i[1]][1]:
                distance[i[1]][1] = cost
                heappush(q, (cost, i[1]))
        else : #짝수이면
            if cost < distance[i[1]][0]:
                distance[i[1]][0] = cost
                heappush(q, (cost, i[1]))

for i in range(1, n+1):
    temp = ""
    if distance[i][1] == INF:
        temp += '-1'
    else:
        temp += str(distance[i][1])
    if distance[i][0] == INF:
        temp += ' -1'
    else:
        temp += ' ' + str(distance[i][0])
    print(temp)