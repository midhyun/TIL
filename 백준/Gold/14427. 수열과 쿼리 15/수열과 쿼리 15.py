import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

def solution():
    N = int(input())
    copyA = [*map(int, input().split())]
    A = [[int(x), i] for i, x in enumerate(copyA)]
    heapify(A)

    M = int(input())

    for _ in range(M):
        query = [*map(int, input().split())]
        if query[0] == 1:
            _, idx, value = query
            copyA[idx-1] = value
            heappush(A, [value, idx-1])
        else:
            while True:
                minVal, minIdx = A[0]
                if copyA[minIdx] == minVal:
                    break
                heappop(A)                
            print(A[0][1]+1)
    return

solution()