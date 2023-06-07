import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):
    visited = [-1] * (N+1)
    visited[cur] = 0
    stack = []
    stack.append(cur)

    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                stack.append(nxt)
    dist = max(visited)
    return [dist, visited.index(dist)]

def solution():
    s_node = dfs(1)[1]
    dist = dfs(s_node)[0]

    return dist - (dist//2)
print(solution())