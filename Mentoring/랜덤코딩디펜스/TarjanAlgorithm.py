import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
id = 0
def dfs_cost(cur, visited):
    global tmp
    for nxt in graph[cur]:
        if nxt in scc and not visited[nxt]:
            visited[nxt] = True
            tmp += cost[cur][nxt]
            dfs_cost(nxt, visited)

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
        scc = set()
        while True:
            x = stack.pop()
            on_stack[x] = False
            scc.add(x)
            if x == cur:
                break

        result.append(scc)

    return parent
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    visited = [-1]*(V+1)
    on_stack = [False]*(V+1)
    stack = []
    graph = [[] for _ in range(V+1)]
    cost = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, x = map(int, input().split())
        graph[a].append(b)
        cost[a][b] = x

    result = []
    for i in range(1, V+1):
        if visited[i] == -1:
            dfs(i)

    res = sys.maxsize
    for scc in result:
        tmp = 0
        visited = [False]*(V+1)
        dfs_cost(list(scc)[0], visited)
        if tmp:
            res = min(res, tmp)

    print(f'#{test_case}', res)