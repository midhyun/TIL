import sys
from collections import deque
sys.stdin = open('16928_뱀과사다리게임.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[i,i] for i in range(101)]
visited = [False]*(101)
result = [0]*101
for _ in range(n+m):
    s, e = map(int, input().split())
    graph[s] = [s,e]
dx = [1,2,3,4,5,6]
q = deque()
q.append(graph[1])
visited[s] = True
while q:
    s, e = q.popleft()
    for k in range(6):
        x = e + dx[k]
        if x < 101 and not visited[x]:
            visited[x] = True
            q.append(graph[x])
            result[x] = result[s] + 1
print(result[100])
