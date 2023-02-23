import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('10265_MT.txt')
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
        scc = 0
        while stack:
            x = stack.pop()
            on_stack[x] = 1
            scc_idx[x] = idx
            scc += 1
            if x == cur:
                if scc > 1:
                    result.append((scc, x))
                break

    return parent

def DFS(cur):
    for nxt in graph[cur]:
        if not visited[nxt]:
            temp.append(nxt)
            visited[nxt] = 1
            DFS(nxt)
    
N, K = map(int, input().split())
info = [*map(int, input().split())] # 2, 3, 4
graph = [[] for _ in range(N+1)]
result = []

for i in range(1, N+1):
    graph[info[i-1]].append(i)
    if info[i-1] == i:
        result.append((1, i))

visited = [0]*(N+1)
on_stack = [0]*(N+1)
scc_idx = [0]*(N+1)
stack = []
id, idx = 0, 0

for i in range(1, N+1):
    if not visited[i]:
        SCC(i)
cmn = []
cmx = []
visited = [0]*(N+1)
for res in result:
    temp = []
    if not visited[res[1]]:
        visited[res[1]] = 1
        temp.append(res[1])
        DFS(res[1])
        cmn.append(res[0])
        cmx.append(len(temp))

wv = [0]
dp = [[0]*(K+1)]
line = [0]*(K+1)
for i in range(len(cmn)):
    for j in range(cmn[i],cmx[i]+1):
        if j > K:
            break


print(cmn, cmx)
for i in range(1, len(wv)):
    w, v = wv[i][0], wv[i][1]
    dp.append(line)
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-j][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[-1][-1])