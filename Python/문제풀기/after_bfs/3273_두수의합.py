import sys
sys.stdin = open('3273_두수의합.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
x = int(input())
nums.sort()
left, right = 0, n-1
cnt = 0

while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        cnt += 1
    if temp < x:
        left += 1
    else:
        right -= 1
print(cnt)