import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('4196_도미노.txt')
input = sys.stdin.readline
# 타잔 알고리즘
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
    # scc를 result리스트에 추가
    if parent == visited[cur]:
        scc = []
        while True:
            x = stack.pop()
            on_stack[x] = False
            scc.append(x)
            if x == cur:
                break
        result.append(scc)

    return parent

T = int(input())
for _ in range(T):
    id = 0
    V, E = map(int, input().split())
    visited = [-1]*(V+1)
    on_stack = [False]*(V+1)
    stack = []
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    result = []
    for i in range(1, V+1):
        if visited[i] == -1:
            dfs(i)
    
    indegree = [0]*(len(result)+1)
    idx = 0
    # 각 scc의 아이디값을 각요소에 부여함
    for scc in result:
        idx += 1
        for i in scc:
            visited[i] = idx
    # 모든 노드를 순회하면서, 인접노드가 다른 scc에 속하는 경우
    # 해당 scc를 밀어주는 indegree += 1
    for i in range(1, V+1):
        for nxt in graph[i]:
            if visited[i] != visited[nxt]:
                indegree[visited[nxt]] += 1
    cnt = 0
    # indegree가 없는 경우 밀어주는 도미노가 없음.
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            cnt += 1
    # cnt가 0일 경우 어떤 도미노를 밀어도 모두 넘어지므로 1출력
    print(cnt) if cnt else print(1)