import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(cur):
    global id
    id += 1
    visited[cur] = id
    on_stack[cur] = True
    stack.append(cur)
    parent = visited[cur]

    for nxt in graph[cur]:
        if visited[nxt] == -1:
            parent = min(parent, DFS(nxt))
        elif on_stack[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[cur]:
        scc = []
        while True:
            x = stack.pop()
            on_stack[x] = False
            scc.append(x)
            if x == cur:
                break
        result.append(scc)
    
    return parent


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1]*(N+1)
on_stack = [False]*(N+1)
stack = []
result = []
id = 0

for i in range(1, N+1):
    if visited[i] == -1:
        DFS(i)

print('Yes') if len(result) == 1 else print('No')