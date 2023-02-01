import sys
from heapq import heappop, heappush
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