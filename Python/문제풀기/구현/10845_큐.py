import sys
from collections import deque
sys.stdin = open('10845_큐.txt')
input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
    order = input().split()
    if order[0] == 'push':
        q.append(order[1])
    if order[0] == 'pop':
        print(q.popleft()) if q else print(-1)
    if order[0] == 'size':
        print(len(q))
    if order[0] == 'empty':
        print(0) if q else print(1)
    if order[0] == 'front':
        print(q[0]) if q else print(-1)
    if order[0] == 'back':
        print(q[-1]) if q else print(-1)
