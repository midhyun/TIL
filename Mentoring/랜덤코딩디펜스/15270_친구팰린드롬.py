import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('15270_친구팰린드롬.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b = map(int, input().split())
    graph.append((a, b))

def solution():
    visited = [False]*(N+1)
    ans = dfs(visited, 0)
    ans += 1 if N > ans else 0
    print(ans)

def dfs(visited, cur):
    if cur == M:
        return 0
    
    result = 0
    
    for i in range(cur, M):
        a, b = graph[i]
        if not visited[a] and not visited[b]:
            visited[a], visited[b] = True, True
            result = max(result, dfs(visited, i+1) + 2)
            visited[a], visited[b] = False, False

    return result

solution()
