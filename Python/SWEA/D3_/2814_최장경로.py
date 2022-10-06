import sys
sys.stdin = open('2814_최장경로.txt')
input = sys.stdin.readline

def dfs(s, cnt):
    global result
    result = max(result, cnt)
    for x in graph[s]:
        if not visited[x]:
            visited[x] = 1
            dfs(x, cnt+1)
            visited[x] = 0



t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    result = 0
    for i in range(1, n+1):
        visited = [0]*(n+1)
        visited[i] = 1
        dfs(i, 1)
        result = max(result, max(visited))
    print(f'#{test_case}', result)