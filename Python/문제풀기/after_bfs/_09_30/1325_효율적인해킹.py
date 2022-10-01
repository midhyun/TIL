import sys
sys.stdin = open('1325_효율적인해킹.txt')
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    i, j = map(int, input().split())
    graph[j].append(i)

result = [0]*(n+1)
for i in range(1, n+1):
    visited = [False]*(n+1)
    visited[i] = True
    temp = 0
    stack = [i]
    while stack:
        k = stack.pop()
        for j in graph[k]:
            if not visited[j]:
                visited[j] = True
                stack.append(j)
                temp += 1
    result[i] = temp
    
for i in range(1, n+1):
    if result[i] == max(result):
        print(i, end=' ')