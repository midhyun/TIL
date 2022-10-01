import sys
from collections import deque
import copy
sys.stdin = open('1021_회전하는큐.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [*map(int, input().split())]
q = deque(range(1,n+1))
result = 0
for i in lst:
    left_q = copy.deepcopy(q)
    right_q = copy.deepcopy(q)
    cnt = 0
    while True:
        if left_q[0] == i:
            left_q.popleft()
            q = left_q
            break
        elif right_q[0] == i:
            right_q.popleft()
            q = right_q
            break
        left_q.append(left_q.popleft())
        right_q.appendleft(right_q.pop())
        cnt += 1
    result += cnt
print(result)
