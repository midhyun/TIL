import sys
from collections import deque
sys.stdin = open('10866_덱.txt')
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    order = input().strip().split()
    if order[0] == 'push_front':
        q.appendleft(order[1])
    elif order[0] == 'push_back':
        q.append(order[1])
    elif order[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else: print(0)
    elif order[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
        