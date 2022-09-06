import sys
sys.stdin = open('24480_깊이우선탐색2.txt')
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
stack=[]
result = [0]*(n+1)
cnt = 1
stack.append(r)
while stack:
    cur = stack.pop()
    if not visited[cur]:
        visited[cur] = True
        result[cur] = cnt
        cnt += 1
        graph[cur] = sorted(graph[cur])
        for i in graph[cur]:
            stack.append(i)

for i in result[1:]:
    print(i)