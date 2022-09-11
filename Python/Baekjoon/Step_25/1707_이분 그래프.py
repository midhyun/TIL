import sys
sys.stdin = open('1707_이분 그래프.txt')
input = sys.stdin.readline

k = int(input())
def dfs():
    cur, col = q.pop()
    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            col = not col
            result[i] = col
            q.append((i,col))
            dfs()


for test_case in range(1,k+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    result = [0]*(v+1)
    q = [(1,False)]
    visited[1] = True
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    dfs()
    x = True
    for i in range(1,v+1):
        for j in graph[i]:
            for k in graph[j]:
                if result[j] == result[k]:
                    x = False
    if x == True:
        print('YES')
    else: print('NO')