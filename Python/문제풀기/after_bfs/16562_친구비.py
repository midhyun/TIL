from collections import deque
import sys
sys.stdin = open('16562_친구비.txt')
input = sys.stdin.readline

n, m ,k = map(int, input().split())
graph = [[] for _ in range(n+1)]
pay = [0]+[*map(int,input().split())]

for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

result = 0
visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        q = deque()
        q.append(i)
        visited[i] = True
        temp = [pay[i]]
        while q:
            cur = q.popleft()
            visited[cur] = True
            for j in graph[cur]:
                temp.append(pay[j])
                if not visited[j]:
                    visited[j] = True
                    q.append(j)
        if len(temp) > 0:
            result += min(temp)

if result > k:
    print('Oh no')
else: print(result)