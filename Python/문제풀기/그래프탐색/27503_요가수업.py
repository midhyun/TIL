import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('27503_요가수업.txt')
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

N, M, C, K = map(int, input().split())
yogas = [*map(int, input().split())]
graph = [[] for _ in range(N*2+1)]
arr = [False]*(N+1)
arr2 = [False]*(N+1)

for yoga in yogas:
    arr[yoga] = True

# (a or b) = -a > b, -b > a 
# a혹은 b중 한개이상이 참이면 됨
# a가 거짓이면 b는 참
# b가 거짓이면 a는 참
for _ in range(C):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)
    arr2[a] = arr2[b] = True
# (a xor b) = a > -b, b > -a
# a가 참이면 b는 거짓, b가 참이면 a는 거짓
# 둘중 한개 만 참이면 됨.
for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(-b)
    graph[b].append(-a)

# 수업이 있고, 대체수업도 있는 경우,
for i in range(1, N+1):
    if arr[i] and not arr2[i]:
        graph[-i].append(i)

id, idx = 0, 0
visited = [0]*(N*2+1)
scc_idx = [0]*(N*2+1)
on_stack = [0]*(N*2+1)
stack = []

for i in range(1, N+1):
    if not visited[i]:
        SCC(i)

for i in range(1, N+1):
    if scc_idx[i] == scc_idx[-i]:
        print("NO")
        break
else:
    print("YES")