import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('6543_그래프의싱크.txt')
input = sys.stdin.readline


def dfs(cur):
    global id, idx
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
        idx += 1
        while True:
            x = stack.pop()
            on_stack[x] = False
            scc_idx[x] = idx
            scc.append(x)
            if x == cur:
                break
        scc.sort()
        result.append(scc)

    return parent

while True:
    id, idx = 0, 0
    VE = [*map(int, input().split())]
    if VE[0] == 0:
        break
    V, E = VE
    visited = [-1]*(V+1)
    scc_idx = [0]*(V+1)
    on_stack = [False]*(V+1)
    stack = []
    graph = [[] for _ in range(V+1)]
    edges = [*map(int, input().split())]
    for i in range(0, E*2, 2):
        graph[edges[i]].append(edges[i+1])

    result = []
    for i in range(1, V+1):
        if visited[i] == -1:
            dfs(i)

    check = [0]*(len(result)+1)
    for i in range(1, V+1):
        for j in graph[i]:
            if scc_idx[i] != scc_idx[j]:
                check[scc_idx[i]] += 1
    ans = []
    for i in range(len(result)):
        if not check[i+1]:
            ans += result[i]
    ans.sort()
    print(*ans)
