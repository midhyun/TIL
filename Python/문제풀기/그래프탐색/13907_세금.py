import sys
sys.stdin = open('13907_세금.txt')
input = sys.stdin.readline

INF = int(1e9)
N, M, K = map(int, input().split())
S, D = map(int, input().split())
edges = []

for _ in range(M):
    edges.append(tuple(map(int, input().split())))

dist = [[INF]*(N+1) for _ in range(N+1)]
dist[0][S] = 0

for i in range(1, N):
    for j in range(M):
        # 시작지점에서 i개의 도시를 거쳐서, j번째 도시로 가는 최단 거리
        dist[i][edges[j][0]] = min(dist[i][edges[j][0]], dist[i-1][edges[j][1]]+ edges[j][2])
        dist[i][edges[j][1]] = min(dist[i][edges[j][1]], dist[i-1][edges[j][0]]+ edges[j][2])

for i in range(K+1):
    mn = INF
    for j in range(N):
        mn = min(mn, dist[j][D])
    print(mn)
    if i == K: break
    P = int(input())
    for j in range(N):
        # 도착점 += 도로숫자 * 세금
        if dist[j][D] < INF:
            dist[j][D] += j * P