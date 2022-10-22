import sys
from collections import deque
sys.stdin = open('14395_4연산.txt')
input = sys.stdin.readline

start, end = map(int, input().split())
INF = int(1e9)
visited = [[]]*(INF+1)

def bfs(start, n, end):
    q = deque()
    q.append((start, n))
    visited[start].append(())
    while q:
        i, path = q.popleft()
        print(visited[i])
        if i == end:
            break
        if 1 <= i+start <= INF:
            visited[i+start].append((i+start, path+'+'))
            q.append((i+start, path+'+'))
        if 1 <= i-start <= INF:
            visited[i-start].append((i-start, path+'-'))
            q.append((i-start, path+'-'))
        if 1 <= i*start <= INF:
            visited[i*start].append((i*start, path+'*'))
            q.append((i*start, path+'*'))
        if 1 <= int(i/start) <= INF:
            visited[int(i/start)].append((int(i/start), path+'/'))
            q.append((int(i/start), path+'/'))

bfs(start, '', end)
print(sorted(visited[end])[0])