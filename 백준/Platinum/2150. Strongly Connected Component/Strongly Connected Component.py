import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
id = 0
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
    
    if parent == visited[cur]:
        css = []
        while True:
            x = stack.pop()
            on_stack[x] = False
            css.append(x)
            if x == cur:
                break
        css.sort()
        css.append(-1)
        result.append(css)

    return parent


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
print(len(result))
result.sort(key=lambda x: x[0])
for i in result:
    print(*i)