import sys
from collections import deque
sys.stdin = open('12851_숨바꼭질2.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100500
visited = [False]*(MAX)
queue = deque()
queue.append((N, 0))

def bfs():
    cnt = 0
    times = 100500
    while queue:
        x, t = queue.popleft()
        visited[x] = True
        if x == K:
            times = min(t, times)
            if t == times:
                cnt += 1
        for i in (x-1, x+1, x*2):
            if 0 <= i < MAX:
                if not visited[i]:
                    queue.append((i, t+1))

    return cnt, times

cnt, times = bfs()

if N == K:
    print(0)
else:
    print(times)

if N == K:
    print(1)
else: 
    print(cnt)