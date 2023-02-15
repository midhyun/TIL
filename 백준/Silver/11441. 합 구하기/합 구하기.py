import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + [*map(int, input().split())]
for i in range(1, N+1):
    nums[i] += nums[i-1]
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(nums[j]-nums[i-1])