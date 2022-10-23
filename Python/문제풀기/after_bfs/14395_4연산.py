import sys
from collections import deque
sys.stdin = open('14395_4연산.txt')
input = sys.stdin.readline

start, end = map(int, input().split())
INF = (end*end)+1
visited = [[] for _ in range(INF+1) ]

def bfs(start, n, end):
    q = deque()
    q.append((start, n))
    visited[start].append(())
    while q:
        i, path = q.popleft()
        if i == end:
            break
        if 1 <= i+i <= INF:
            visited[i+i].append(path+'+')
            q.append((i+i, path+'+'))
        if 1 <= i-i <= INF:
            visited[i-i].append(path+'-')
            q.append((i-i, path+'-'))
        if 1 <= i*i <= INF:
            visited[i*i].append(path+'*')
            q.append((i*i, path+'*'))
        if 1 <= int(i/i) <= INF:
            visited[int(i/i)].append(path+'/')
            q.append((int(i/i), path+'/'))

bfs(start, '-1', end)
x = sorted(visited[end])[0]
if len(visited[end]) == 0:
    print(0)
else:
    print(x)