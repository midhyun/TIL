import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('3977_축구전술.txt')
input = sys.stdin.readline

def DFS(cur):
    global id, scc_id
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
            visited[x] = scc_id
            scc.append(x)
            if x == cur:
                scc_id += 1
                break
        result.append(scc)
    
    return parent

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    visited = [-1]*N
    on_stack = [False]*N
    stack = []
    result = []
    id = 0
    scc_id = 0

    for i in range(N):
        if visited[i] == -1:
            DFS(i)
    
    indegree = [0]*(len(result))
    for i in range(N):
        for j in graph[i]:
            if visited[i] != visited[j]:
                indegree[visited[j]] += 1

    if indegree.count(0) == 1:
        for i in range(len(result)):
            if indegree[i] == 0:
                for i in sorted(result[i]):
                    print(i)
    else: print('Confused')
    if test != T-1:
        input()
    print()
            