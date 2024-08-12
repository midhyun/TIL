import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    visited = [False]*100001
    q = [(0, N)]
    while q:
        t, x = heappop(q)
        if x == K:
            return t
        for nxt in ((t, x*2), (t+1, x-1), (t+1, x+1)):
            if 0<= nxt[1] <= 100000 and not visited[nxt[1]]:
                visited[nxt[1]] = True
                heappush(q, nxt)

print(solution())