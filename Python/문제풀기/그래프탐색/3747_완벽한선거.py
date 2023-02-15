import sys
sys.stdin = open('3747_완벽한선거.txt')

def SCC(cur):
    global id, idx
    id += 1
    visited[cur] = id
    parent = id
    stack.append(cur)

    for nxt in graph[cur]:
        if visited[nxt] == -1:
            parent = min(parent, SCC(nxt))
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

input = map(int, sys.stdin.read().split())

while True:
    try: N = next(input)
    except : break
    M = next(input)
    graph = [[] for _ in range(N*2+1)]
    for i in range(1, M+1):
        a, b = next(input), next(input)
        graph[-a].append(b)
        graph[-b].append(a)

    id, idx = 0, 0
    visited = [-1]*(N*2+1)
    on_stack = [0]*(N*2+1)
    scc_idx = [0]*(N*2+1)
    stack = []

    for i in range(1, N*2+1):
        if visited[i] == -1:
            SCC(i)
    
    for i in range(1, N+1):
        if scc_idx[i] == scc_idx[-i]:
            print(0)
            break
    else:
        print(1)