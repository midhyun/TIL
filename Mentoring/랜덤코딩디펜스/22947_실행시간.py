import sys
from collections import deque
sys.stdin = open('22947_실행시간.txt')
input = sys.stdin.readline

def topolgy(_indegree, adj, times, startNode, endNode):
    indegree = _indegree[:]
    result = [0]*(len(adj))
    result[startNode] = times[startNode]
    q = deque([startNode])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            result[nxt] = max(result[nxt], result[cur])
            indegree[nxt] -= 1
            if (indegree[nxt] == 0):
                result[nxt] += times[nxt]
                q.append(nxt)
            
    return result[endNode]

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
    indegree = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        indegree[b] += 1
        adj[a].append(b)

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