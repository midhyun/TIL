import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [*map(int, input().split())]
heapq.heapify(nums)
for _ in range(m):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    temp = x + y
    heapq.heappush(nums, temp)
    heapq.heappush(nums, temp)

print(sum(nums))