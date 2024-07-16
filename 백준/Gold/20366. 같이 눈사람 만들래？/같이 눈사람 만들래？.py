import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    heights = list(map(int, input().split()))
    heights.sort()
    min_diff = sys.maxsize

    for i in range(N):
        for j in range(i+3, N):
            left, right = i+1, j-1
            while left < right:
                diff = heights[i] + heights[j] - heights[left] - heights[right]
                min_diff = min(min_diff, abs(diff))

                if diff < 0: right -= 1
                else: left += 1
    
    print(min_diff)

solution()
