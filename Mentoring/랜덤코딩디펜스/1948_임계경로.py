import sys
from collections import deque
sys.stdin = open('1948_임계경로.txt')
input = sys.stdin.readline

def solution():
    N, M = int(input()), int(input())
    dp = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    for _ in range(M):
        # 출발, 도착, 시간
        s, a, t = map(int, input().split())
        graph[s].append((a, t))
        rev_graph[a].append((s, t))
        indegree[a] += 1

    start_city, arrive_city = map(int, input().split())
    
    q = deque()
    q.append(start_city)
    path = [[] for _ in range(N+1)]
    while q:
        cur = q.popleft()

        for nxt, nxt_time in graph[cur]:
            indegree[nxt] -= 1
            nxt_dist = dp[cur] + nxt_time

            if dp[nxt] == nxt_dist:
                path[nxt].append(cur)
            elif dp[nxt] < nxt_dist:
                dp[nxt] = nxt_dist
                path[nxt] = [cur]

            if not indegree[nxt]:
                q.append(nxt)

    edge = 0
    stack = [arrive_city]
    visited = [False] * (N+1)

    while stack:
        cur = stack.pop()
        for pre in path[cur]:
            edge += 1
            if not visited[pre]:
                visited[pre] = True
                stack.append(pre)

    print(dp[arrive_city])
    print(edge)

solution()