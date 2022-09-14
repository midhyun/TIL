import sys
import heapq
sys.stdin = open('11279_최대힙.txt')
input = sys.stdin.readline
q = []
n = int(input())
for i in range(n):
    x = -int(input())
    if x == 0:
        if len(q) > 0:
            print(-heapq.heappop(q))
        else: print(0)
    else:
        heapq.heappush(q, x)