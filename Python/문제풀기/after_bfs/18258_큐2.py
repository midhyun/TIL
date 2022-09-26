import sys
from collections import deque
sys.stdin = open('18258_큐2.txt')
input = sys.stdin.readline

q = deque()
n = int(input())
for i in range(n):
    order = input().strip().split()
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else: print(0)
    elif order[0] == 'front':
        if len(q) == 0:
            print(-1)
        else: print(q[0])
    elif order[0] == 'back':
        if len(q) == 0:
            print(-1)
        else: print(q[-1])