import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('2207_가위바위보.txt')
input = sys.stdin.readline

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
            scc_idx[x] = idx
            on_stack[x] = 1
            if x == cur:
                break
    
    return parent
    
M, N = map(int, input().split())
graph = [[] for _ in range(N*2+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)
    
scc_idx = [0]*(N*2+1)
on_stack = [0]*(N*2+1)
visited = [-1]*(N*2+1)
stack = []
id, idx = 0, 0

for i in range(1, N*2+1):
    if visited[i] == -1:
        SCC(i)

for i in range(1, N+1):
    if scc_idx[i] == scc_idx[-i]:
        print('OTL')
        break
else:
    print('^_^')