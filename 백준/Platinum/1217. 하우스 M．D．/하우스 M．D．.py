import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def SCC(cur):
    global id, idx
    id += 1
    visited[cur] = id
    parent = id
    stack.append(cur)

    for nxt in graph[cur]:
        if not visited[nxt]:
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


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    graph = [[] for _ in range(M*2+1)]
    for _ in range(N):
        a, b = map(int, input().split())
        graph[-a].append(b)
        graph[-b].append(a)

    visited = [0]*(M*2+1)
    scc_idx = [0]*(M*2+1)
    on_stack = [0]*(M*2+1)
    stack = []
    id, idx = 0, 0
    
    for i in range(1, M*2+1):
        if not visited[i]:
            SCC(i)

    for i in range(1, M+1):
        if scc_idx[i] == scc_idx[-i]:
            print(0)
            break
    else:
        print(1)