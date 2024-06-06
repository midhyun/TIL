import sys
from heapq import heappush, heappop
sys.stdin = open('21924_도시 건설.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
# 모든 간선의 비용의 합.
total_cost = 0
# 그래프 초기화.
for _ in range(M):
    A, B, C = map(int, input().split())
    heappush(graph[A], (C, B))
    heappush(graph[B], (C, A))
    total_cost += C

def solution():
    # 최소 스패닝 트리의 비용
    answer = 0
    # 현재까지 방문한 노드의 수
    cnt = 0
    heap = [(0, 1)]
    while heap:
        # 모든 노드를 방문했을 때 종료.
        if cnt == N:
            break
        # 현재 노드의 비용과 노드 번호.
        cost, node = heappop(heap)
        # 이미 방문한 노드라면 넘어감.
        if visited[node]:
            continue
        # 방문처리, 비용추가, 노드수 카운트.
        visited[node] = True
        answer += cost
        cnt += 1
        # 현재 노드에서 다음 노드의 간선을 힙에 추가.
        for c, n in graph[node]:
            if not visited[n]:
                heappush(heap, (c, n))
    # 모든 노드를 방문하지 못했다면 -1 반환.
    if cnt != N:
        return -1

    return total_cost-answer

print(solution())