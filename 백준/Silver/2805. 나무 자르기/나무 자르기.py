import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = [*map(int, input().split())]

low = 0
high = max(heights)

while low <= high:
    mid = (low + high) // 2

    takes = 0
    for i in range(N):
        if heights[i] > mid:
            takes += heights[i] - mid

    if takes >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)