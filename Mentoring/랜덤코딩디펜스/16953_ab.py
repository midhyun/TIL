import sys
from collections import deque
sys.stdin = open('16953_ab.txt')
input = sys.stdin.readline

A, B = map(int, input().split())

def bfs():
    q = deque()
    q.append((A, 0))
    while q:
        x, cnt = q.popleft()
        if x == B:
            return cnt + 1

        if x <= B:
            q.append((x*2, cnt+1))
            q.append((x*10+1, cnt+1))
    
    return -1

print(bfs())