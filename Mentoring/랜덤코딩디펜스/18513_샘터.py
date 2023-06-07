import sys
from collections import deque
sys.stdin = open('18513_샘터.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
pond = set(map(int, input().split()))
q = deque()
for i in pond:
    q.append((i, -1))
    q.append((i, 1))
cnt, result = 0, 0
while cnt < K:
    cur, dir = q.popleft()
    
    if cur+dir not in pond:
        cnt += 1
        result += abs(dir)
        pond.add(cur+dir)
        if dir > 0:
            q.append((cur, dir+1))
        else: q.append((cur, dir-1))
        
print(result)