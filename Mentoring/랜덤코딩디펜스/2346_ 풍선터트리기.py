import sys
from collections import deque
sys.stdin = open('2346_ 풍선터트리기.txt')
input = sys.stdin.readline

# 풍선이 N개 원형으로 놓여져 있음.
# 1번부터 N번 풍선까지
# 1 <= N <= 1000

N = int(input())
papers = [*map(int, input().split())]

q = deque()
for num, paper in enumerate(papers, 1):
    q.append((paper, num))
while q:
    n, x = q.popleft()
    print(x, end=' ')
    if not q:
        break

    if n > 0:
        for _ in range(n-1):
            tmp = q.popleft()
            q.append(tmp)
    else:

        for _ in range(abs(n)):
            tmp = q.pop()
            q.appendleft(tmp)
