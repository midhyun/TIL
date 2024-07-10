import sys
sys.stdin = open('1613_역사.txt')
input = sys.stdin.readline
# python3 제출 시간초과, pypy3 통과
# 플루이드 워셜 알고리즘
def solution():
    INF = sys.maxsize
    N, K = map(int, input().split())
    # 2차원 거리 배열을 무한대로 초기화 하고 자기자신은 0
    distance = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                distance[i][j] = 0
    # 거리정보를 입력받아 초기화
    for _ in range(K):
        a, b = map(int, input().split())
        distance[a][b] = 1
    # 플루이드 워셜 알고리즘 dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    # i 에서 j로 가는 최단거리는 i에서 k를 거쳐 j로 가는 거리와 i에서 j로 가는 거리 중 작은 값으로 비교.
    # k, i, j 는 1 ~ N+1
    # N^3 시간 복잡도
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # S개의 쌍에 대해 거리 정보 출력
    # pre -> post 로 가는 거리가 INF 보다 작으면 pre가 post 보다 먼저 일어난 사건
    S = int(input())
    for _ in range(S):
        pre, post = map(int, input().split())
        if distance[pre][post] < INF:
            print(-1)
        elif distance[post][pre] < INF:
            print(1)
        else:
            print(0)

# dfs 풀이
def solution_dfs():
    # 재귀 dfs, 자식 노드를 방문하면서 부모 노드에 자식 노드를 추가함.
    # 마지막에 부모 노드에 자식 노드를 추가한 집합을 반환.
    def dfs(node):
        if not visited[node]:
            visited[node] = True
            for nxt in graph[node]:
                canVisit[node].add(nxt)
                canVisit[node].update(dfs(nxt))
        return canVisit[node]
    
    N, K = map(int, input().split())
    visited = [False] * (N+1)
    graph = [[] for _ in range(N+1)]
    canVisit = [set() for _ in range(N+1)]
    # 간선 그래프 정보 입력
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
    # dfs 탐색
    for node in range(1, N+1):
        if not visited[node]:
            dfs(node)
    
    for _ in range(int(input())):
        pre, post = map(int, input().split())
        if post in canVisit[pre]:
            print(-1)
        elif pre in canVisit[post]:
            print(1)
        else:
            print(0)

solution_dfs()
