import sys
import heapq                                        # 힙으로 성능 향상
sys.stdin = open('1916_최소비용.txt')
input = sys.stdin.readline

N = int(input())                                    # 노드의 개수
M = int(input())                                    # 간선의 개수
INF = 1e9
graph = [[] for _ in range(N+1)]                    # 인접 노드 리스트
distance = [INF] * (N+1)                            # 비용을 담아줄 리스트

for i in range(M):
    a, b, c = map(int, input().split())             # a에서 b노드에 가는데 c만큼의 비용 발생
    graph[a].append((b, c))                         # 리스트의 a인덱스에 b, c 튜플 추가

start , end = map(int, input().split())

def dijkstra(start):                                # 다익스트라 알고리즘 함수 생성
    q = []                                          # 힙을 담을 큐리스트
    heapq.heappush(q, (0, start))                   # 힙에 (0, start) 거리와 시작지점을 넣어줌. (시작지점에서의 거리는 0)
    while q:                                        # 큐에 값이 있다면 탐색
        dist, now = heapq.heappop(q)                # 거리(dist)와 현재노드(now)의 위치 부터 탐색 시작
        if distance[now] < dist:                    # 현재 노드의 distance 리스트에 저장된 거리가, dist 보다 작다면 다음 루프로 넘어감 (continue)
            continue
        for i in graph[now]:                        # 현재 노드의 인접리스트를 순회함,
            cost = dist + i[1]                      # 전체 비용은 이전 노드까지의 최소비용 + 이전노드에서 현재노드로 이동하는데 소모한 비용
            if cost < distance[i[0]]:               # 이때 다른 노드를 거쳐 이동했을 때 더 작은 비용이 발생했다면 그 중 작은 값으로 대체함
                distance[i[0]] = cost               # 더 작은 비용이 발생 했다면, 힙에 넣어서 탐색함.
                heapq.heappush(q, (cost, i[0]))     # cost는 distance 리스트의 인덱스(해당하는 노드위치) 에 저장함.
                                                    # 더 이상 작은 비용이 발생하지 않는다면 큐에 담을 수 없으므로 큐가 비어서 반복 종료.
dijkstra(start)

for i in range(N+1):
    if i == end:
        print(distance[i])