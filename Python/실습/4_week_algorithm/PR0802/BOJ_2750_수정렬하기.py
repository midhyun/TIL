import sys
import heapq
sys.stdin = open('2750.txt')
input = sys.stdin.readline
N = int(input())
lst = []

for i in range(N):
    heapq.heappush(lst, int(input()))   # 힙으로 값을 추가해줌

for i in range(N):
    print(heapq.heappop(lst))           # 최소힙에서 하나씩 팝, 프린트 하므로 오름차순으로 프린트됨.

# for i in range(N):                    # 리스트 정렬방법
#     lst.append(int(input()))
# lst.sort()
# for j in lst:
#     print(j)