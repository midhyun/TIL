import sys
input = sys.stdin.readline

def getTakes(mid):
    takes = 0
    for height in heights:
        if height > mid:
            takes += height - mid
    return takes

N, M = map(int, input().split())
heights = [*map(int, input().split())]

def solution():
    low = 0
    high = max(heights)

    while low <= high:
        mid = (low + high) // 2

        takes = getTakes(mid)

        if takes >= M:
            low = mid + 1
        else:
            high = mid - 1

    return high

print(solution())