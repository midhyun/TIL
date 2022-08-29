import sys
sys.stdin = open('11054_바이토닉부분수열.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]

dp_up = [0] *n
dp_down = [0] *n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp_up[i] < dp_up[j]:
            dp_up[i] = dp_up[j]
    dp_up[i] += 1
nums = nums[::-1]
for i in range(n):
    for j in range(n):
        if nums[i] > nums[j] and dp_down[i] < dp_down[j]:
            dp_down[i] = dp_down[j]
    dp_down[i] += 1
dp_down = dp_down[::-1]
result = 0

for i in range(n):
    result = max(result, dp_up[i] + dp_down[i])

print(result-1)