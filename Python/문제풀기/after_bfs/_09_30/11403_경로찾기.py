import sys
sys.stdin = open('11403_경로찾기.txt')
input = sys.stdin.readline

n = int(input())
result = [[0]*n for _ in range(n)]
graph = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(n):
    in_node = [*map(int, input().split())]
    for j in range(n):
        if in_node[j] == 1:
            graph[i].append(j)

def dfs(start):
    visit = [False]*n
    stack = [start]
    while stack:
        x = stack.pop()
        for i in graph[x]:
            if not visit[i]:
                visit[i] = True
                stack.append(i)
                visited[start][i] = 1

for i in range(n):
    dfs(i)

for i in visited:
    for j in i:
        print(j, end=' ')
    print()