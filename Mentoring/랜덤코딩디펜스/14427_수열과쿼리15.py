import sys
sys.stdin = open('14427_수열과쿼리15.txt')
input = sys.stdin.readline
from heapq import heappop, heappush, heapify
# 힙 자료구조
def solution():
    N = int(input())
    # copyA 는 값이 들어있는 리스트
    # A는 [값, 인덱스]가 들어있는 힙 자료구조
    copyA = [*map(int, input().split())]
    A = [[int(x), i] for i, x in enumerate(copyA)]
    heapify(A)

    M = int(input())

    for _ in range(M):
        query = [*map(int, input().split())]
        # 값을 바꿔주고 힙에 바꾼 값을 추가한다.
        if query[0] == 1:
            _, idx, value = query
            copyA[idx-1] = value
            heappush(A, [value, idx-1])
        else:
            # 1쿼리에서 변경한 값을 추가만 했기 때문에 기존의 값이 남아있다.
            # 최신화된 값인 copyA와 비교해서 값이 다르면 heappop을 한다.
            # 최소값이 아닌 최신화가 안된 값은 결과와 상관 없다.
            while True:
                minVal, minIdx = A[0]
                if copyA[minIdx] == minVal:
                    break
                heappop(A)                
            print(A[0][1]+1)
    return

solution()
