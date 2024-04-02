import sys
from collections import deque
sys.stdin = open('2252_줄세우기.txt')
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    q = deque()
    result = []
    for _ in range(M):
        A, B = map(int, input().split())
        indegree[B] += 1
        graph[A].append(B)

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    for i in range(1, N+1):
        if not q:
            break
        
        cur = q.popleft()
        result.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    print(*result)

solution()    
