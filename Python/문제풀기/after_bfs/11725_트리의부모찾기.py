import sys
sys.stdin = open('11725_트리의부모찾기.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(n-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            parent[i] = start
            dfs(i)
dfs(1)
for i in parent[2:]:
    print(i)