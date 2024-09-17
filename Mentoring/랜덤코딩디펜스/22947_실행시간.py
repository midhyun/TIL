import sys
from collections import deque
sys.stdin = open('22947_실행시간.txt')
input = sys.stdin.readline

# 위상정렬 알고리즘 + 시간 적용
def topolgy(_indegree, adj, times, startNode, endNode):
    indegree = _indegree[:]
    result = [0]*(len(adj))
    result[startNode] = times[startNode]
    q = deque([startNode])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            # 현재 노드까지의 작업을 완료 했을 때, 
            result[nxt] = max(result[nxt], result[cur])
            indegree[nxt] -= 1
            # 진입차수가 0 이면, 큐에 추가.
            if (indegree[nxt] == 0):
                result[nxt] += times[nxt]
                q.append(nxt)
            
    return result[endNode]

# 노드 작업시간 0초로 바꾸면서 백트래킹 K는 최대 3이므로,
def calc_min(adj, indegree, times, idx, startNode, endNode, k):
    global ans
    if (k == 0):
        ans = min(ans, topolgy(indegree, adj, times, startNode, endNode))
    else:
        for i in range(idx+1, len(adj)):
            if (i == endNode):
                continue
            temp = times[i]
            times[i] = 0
            calc_min(adj, indegree, times, i, startNode, endNode, k-1)
            times[i] = temp

def solution():
    times = [0]+[*map(int, input().split())]
    adj = [[] for _ in range(N+1)]
    indegree = [0]*(N+1) # 진입차수가 0이면 작업가능
    for _ in range(M):
        a, b = map(int, input().split())
        indegree[b] += 1
        adj[a].append(b)

    # 시작노드와 종료노드 탐색
    startNode = 0
    endNode = 0
    for i in range(1, N+1):
        if indegree[i] == 0:
            startNode = i
            break
    for i in range(1, N+1):
        if len(adj[i]) == 0:
            endNode = i
            break
    calc_min(adj, indegree, times, 1, startNode, endNode, K)
    
    print(ans)

    return

N, M, K = map(int, input().split())
ans = 1e9

solution()