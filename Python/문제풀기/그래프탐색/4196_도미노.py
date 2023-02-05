import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('4196_도미노.txt')
input = sys.stdin.readline

def dfs(cur):
    global id
    id += 1
    visited[cur] = id
    stack.append(cur)
    on_stack[cur] = True
    parent = visited[cur]
    for nxt in graph[cur]:
        if visited[nxt] == -1:
            parent = min(parent, dfs(nxt))
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

T = int(input())
for _ in range(T):
    id = 0
    V, E = map(int, input().split())
    visited = [-1]*(V+1)
    on_stack = [False]*(V+1)
    stack = []
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    result = []
    for i in range(1, V+1):
        if visited[i] == -1:
            dfs(i)
    
    indegree = [0]*(len(result)+1)
    idx = 0
    for scc in result:
        idx += 1
        for i in scc:
            visited[i] = idx

    for i in range(1, V+1):
        for nxt in graph[i]:
            if visited[i] != visited[nxt]:
                indegree[visited[nxt]] += 1
    cnt = 0
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            cnt += 1
    print(cnt) if cnt else print(1)