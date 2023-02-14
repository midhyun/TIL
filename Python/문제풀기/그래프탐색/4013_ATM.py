import sys
from collections import deque
sys.setrecursionlimit(10**7)
sys.stdin = open('4013_ATM.txt')
input = sys.stdin.readline

def dfs(cur):
    global id, idx
    id += 1
    stack.append(cur)
    visited[cur] = id
    parent = id

    for nxt in graph[cur]:
        if visited[nxt] == -1:
            parent = min(parent, dfs(nxt))
        elif not on_stack[nxt]:
            parent = min(parent, visited[nxt])
    
    if parent == visited[cur]:
        idx += 1
        temp = 0
        while stack:
            x = stack.pop()
            scc_idx[x] = idx
            on_stack[x] = 1
            temp += atm[x]
            if x == cur:
                scc.append(temp)
                break
    
    return parent

def dfs_scc(cost, cur):
    if visited_in[cur] > cost: return
    for nxt in indegree_graph[cur]:
        visited_in[nxt] = max(visited_in[nxt], visited_in[cur]+scc[nxt])
        dfs_scc(visited_in[nxt], nxt)
    

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
atm = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, N+1):
    atm[i] = int(input())

S,P = map(int, input().split())
rest = [*map(int, input().split())]
visited = [-1]*(N+1)
on_stack = [0]*(N+1)
scc_idx = [0]*(N+1)
scc = [0]
stack = []
id, idx = 0, 0

for i in range(1, N+1):
    if visited[i] == -1:
        dfs(i)

indegree_graph = [[] for _ in range(len(scc))]
visited_in = [0]*len(scc)

for i in range(1, N+1):
    for nxt in graph[i]:
        if scc_idx[i] != scc_idx[nxt]:
            indegree_graph[scc_idx[i]].append(scc_idx[nxt])

visited_in[scc_idx[S]] = scc[scc_idx[S]]
dfs_scc(scc[scc_idx[S]], scc_idx[S])

# q = deque()
# q.append((scc[scc_idx[S]], scc_idx[S]))
# while q:
#     cost, cur = q.popleft()
#     if visited_in[cur] > cost : continue

#     for nxt in indegree_graph[cur]:
#         if visited_in[nxt] < cost + scc[nxt]:
#             visited_in[nxt] = cost + scc[nxt]
#             q.append((cost + scc[nxt], nxt))

result = 0
for outback in rest:
    result = max(result, visited_in[scc_idx[outback]])

print(result)