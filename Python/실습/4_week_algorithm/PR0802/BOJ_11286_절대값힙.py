import sys
import heapq
sys.stdin = open('11286.txt')
input = sys.stdin.readline
N = int(input())

heap = []
heapq.heapify(heap)

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))   # 절대값이 가장 작은값 순서로 정렬, 원래값도 같이 튜플형태로 추가 
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])   # 절대값이 같은 숫자중 더 작은 값을 꺼내기 위해