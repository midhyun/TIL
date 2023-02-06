import sys
sys.setrecursionlimit(10**7)
from collections import deque
input = sys.stdin.readline

def DFS(cur):
    global id, idx
    id += 1
    visited[cur] = id
    stack.append(cur)
    parent = visited[cur]

    for nxt in graph[cur]:
        if visited[nxt] == -1:
            parent = min(parent, DFS(nxt))
        elif not check[nxt]:
            parent = min(parent, visited[nxt])
    
    if parent == visited[cur]:
        idx += 1
        temp = []
        while stack:
            x = stack.pop()
            scc_idx[x] = idx
            check[x] = 1
            temp.append(x)
            if x == cur:
                break
        scc.append(temp)
    
    return parent

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = len(scc[start])
    while q:
        cur = q.popleft()
        for i in scc_graph[cur]:
            if visited[i] < visited[cur] + len(scc[i]):
                visited[i] = visited[cur] + len(scc[i])
                q.append(i)

N, M, S, T = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

id, idx = 0, 0
visited = [-1]*(N+1)
check = [0]*(N+1)
scc_idx = [0]*(N+1)
stack = []
scc = [[]]

for i in range(1, N+1):
    if visited[i] == -1:
        DFS(i)

scc_graph = [[] for _ in range(len(scc))]
for i in range(1, N+1):
    for j in graph[i]:
        if scc_idx[i] != scc_idx[j]:
            scc_graph[scc_idx[i]].append(scc_idx[j])

if S == T:
    print(len(scc[scc_idx[S]]))
else:
    visited = [0]*(len(scc))
    BFS(scc_idx[S])
    print(visited[scc_idx[T]])