import sys
from collections import deque
sys.stdin = open('5014_스타트링크.txt')
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [False]*(f+1)
graph = [0]*(f+1)
dx = [u, -d]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        i = q.popleft()
        for k in range(2):
            x = i + dx[k]
            if 1 <= x < (f+1) and not visited[x]:
                visited[x] = True
                q.append(x)
                graph[x] = graph[i] + 1
                if x == g:
                    return
bfs(s)
if graph[g] == 0 and not visited[g]:
    print('use the stairs')
else:
    print(graph[g])