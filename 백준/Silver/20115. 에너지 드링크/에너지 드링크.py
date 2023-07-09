import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
nums.sort()
result = nums[-1]
for i in range(N-1):
    result += nums[i]/2

print(result)