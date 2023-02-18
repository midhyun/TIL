import sys
sys.stdin = open('11097_도시계획.txt')
input = sys.stdin.readline
# SCC의 발견 조건은 '자신의 자식 정점들이 
# 자신의 부모 정점으로 갈 수 있는 경우가 없는 경우'
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
        scc = []
        while stack:
            x = stack.pop()
            on_stack[x] = 1
            scc_idx[x] = idx
            scc.append(x)
            if x == cur:
                break

        if len(scc) > 1:
            for i in range(len(scc)-1, -1, -1):
                result.append((scc[i-1], scc[i]))
    
    return parent

T = int(input())    
for test in range(T):
    input()
    N = int(input())
    matrix = [[*map(int, list(input().strip()))] for _ in range(N)]
    graph = [[] for _ in range(N+1)]
    
    for i in range(N):
        matrix[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if matrix[i][j] and matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                graph[i+1].append(j+1)

    id, idx = 0, 0
    visited = [-1]*(N+1)
    on_stack = [0]*(N+1)
    scc_idx = [0]*(N+1)
    stack = []
    result = []
    
    for i in range(1, N+1):
        if visited[i] == -1:
            SCC(i)

    for i in range(1, N+1):
        for j in graph[i]:
            if scc_idx[i] != scc_idx[j]:
                result.append((i, j))

    print(len(result))
    for res in result:
        print(*res)
    if test < T-1:
        print()