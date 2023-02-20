import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('16915_호텔관리.txt')
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
        if not on_stack[nxt]:
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


N, M = map(int, input().split())
lock = [*map(int, input().split())]
switches = [[] for _ in range(N+1)]
graph = [set() for _ in range(M*2+1)]
# 중복방지를 위해 graph에 set()로 간선을 넣음
# 각 방과 연결된 스위치 2개 입력
for i in range(1, M+1):
    info = [*map(int, input().split())]
    for j in range(1, len(info)):
        switches[info[j]].append(i)
# 방의 상태에 따라서 간선 입력
# 문이 열려있다면 두개의 스위치 모두 누르거나 누르지않아야함.
# 문이 닫혀있다면 한개의 스위치는 반드시 눌러야 함.
for i in range(1, N+1):
    a, b = switches[i]
    if lock[i-1]:
        graph[a].add(b)
        graph[b].add(a)
        graph[-a].add(-b)
        graph[-b].add(-a)
    else:
        graph[a].add(-b)
        graph[-a].add(b)
        graph[-b].add(a)
        graph[b].add(-a)

id, idx = 0, 0
visited = [-1]*(M*2+1)
scc_idx = [0]*(M*2+1)
on_stack = [0]*(M*2+1)
stack = []

for i in range(1, M*2+1):
    if visited[i] == -1:
        SCC(i)

for i in range(1, M+1):
    if scc_idx[i] == scc_idx[-i]:
        print(0)
        break
else:
    print(1)