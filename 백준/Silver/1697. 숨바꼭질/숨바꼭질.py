import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100500
visited = [False]*(MAX)
queue = deque()
queue.append((N, 0))

def bfs():
    while queue:
        x, t = queue.popleft()
        if x == K:
            return t
        for i in (x-1, x+1, x*2):
            if 0 <= i < MAX and not visited[i]:
                visited[i] = True
                queue.append((i, t+1))
print(bfs())