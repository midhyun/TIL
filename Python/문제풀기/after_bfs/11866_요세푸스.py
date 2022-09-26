import sys
from collections import deque
sys.stdin = open('11866_요세푸스.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1,n+1))
lst = []
cnt = 0
while q:
    cnt += 1
    if cnt == k:
        cnt = 0
        lst.append(q.popleft())
    else:
        q.append(q.popleft())

print(f"<{', '.join(map(str, lst))}>")