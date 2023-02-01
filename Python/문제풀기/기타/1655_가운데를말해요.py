import sys
from heapq import heappop, heappush
sys.stdin = open('1655_가운데를말해요.txt')
input = sys.stdin.readline

N = int(input())
minq = []
maxq = []

for _ in range(N):
    x = int(input())
    if len(maxq) == len(minq):
        heappush(maxq, -x)
    else:
        heappush(minq, x)
    
    if minq and maxq and -maxq[0] > minq[0]:
        x = heappop(maxq)
        y = heappop(minq)

        heappush(maxq, -y)
        heappush(minq, -x)
    print(-maxq[0])