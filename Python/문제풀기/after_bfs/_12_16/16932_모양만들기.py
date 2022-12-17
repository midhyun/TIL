import sys
from collections import deque
sys.stdin = open('16932_모양만들기.txt')
input = sys.stdin.readline

n = int(input())

def bfs(n):
    q = deque()
    q.append((1,0,0))
    set_ = set()
    set_.add((1,0))
    while q:
        now, clip, times = q.popleft()
        if now == n:
            return times
        if (now, now) not in set_:
            q.append((now, now, times+1))
            set_.add((now, now))
        if clip != 0 and (now + clip, clip) not in set_:
            q.append((now + clip, clip, times+1))
            set_.add((now + clip, clip))
        if (now-1, clip) not in set_:
            q.append((now-1, clip, times+1))
            set_.add((now-1, clip))

print(bfs(n))