import sys
sys.stdin = open('1506_경찰서.txt')
input = sys.stdin.readline
id = 0

def DFS(start):
    global id
    id += 1
    scc.append(start)
    visited[start] = id
    on_scc[start] = True
    parent = visited[start]
    for i in range(N):
        if graph[start][i] == '1' and visited[i] == -1:
            parent = min(parent, DFS(i))
        elif graph[start][i] == '1' and on_scc[i]:
            parent = min(parent, visited[i])
    
    if parent == visited[start]:
        temp = int(1e6)
        while True:
            x = scc.pop()
            on_scc[x] = False
            temp = min(temp, costs[x])
            if start == x:
                break
        result.append(temp)
    return parent


N = int(input())
costs = [*map(int, input().split())]
graph = [list(input().strip()) for _ in range(N)]
visited = [-1]*N
on_scc = [False]*N
scc = []

result = []
for i in range(N):
    if visited[i] == -1:
        DFS(i)

print(sum(result))