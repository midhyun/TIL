import sys
sys.stdin = open('24479_깊이우선탐색1.txt')
input = sys.stdin.readline

n, m, r = map(int ,input().split())
graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
stack = []
result = [0] *(n+1)
cnt = 1
stack.append(r)
visited[r] = True
while stack:
    cur = stack.pop()
    result[cur] = min(result[cur],cnt)
    cnt += 1
    graph[cur] = sorted(graph[cur], reverse=True)
    for i in graph[cur]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True
for i in result[1:]:
    print(i)
