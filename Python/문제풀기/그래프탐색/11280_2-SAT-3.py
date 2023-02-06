import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('11280_2-SAT-3.txt')
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
        elif not on_stack[nxt]:
            parent = min(parent, visited[nxt])
    
    if parent == visited[cur]:
        idx += 1
        while stack:
            x = stack.pop()
            on_stack[x] = 1
            scc_idx[x] = idx
            if x == cur:
                break
    
    return parent

N, M = map(int, input().split())
graph = [[] for _ in range(N*2+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)

id, idx = 0, 0
visited = [-1] * (N*2 + 1)
on_stack = [0] * (N*2 + 1)
scc_idx = [0] * (N*2 + 1)
stack = []

for i in range(1, N+1):
    if visited[i] == -1:
        DFS(i)

for i in range(1, N+1):
    if scc_idx[i] == scc_idx[-i]:
        print(0)
        break
else:
    print(1)