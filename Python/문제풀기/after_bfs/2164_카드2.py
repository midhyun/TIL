import sys
from collections import deque
sys.stdin = open('2164_카드2.txt')
input = sys.stdin.readline

n = int(input())
q = deque(range(1,n+1))
for i in range(n-1):
    q.popleft()
    top = q.popleft()
    q.append(top)
print(q.popleft())