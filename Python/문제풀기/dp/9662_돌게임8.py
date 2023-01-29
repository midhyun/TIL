import sys
sys.stdin = open('9662_돌게임8.txt')
input = sys.stdin.readline

m = int(input())
k = int(input())
nums = [*map(int, input().split())]
dp = [0] *(6544)
temp = [nums[0]]
now = nums[0]
dp[now] = 1

for i in range(1, k):
    for j in range(now+1, nums[i]):
        if 0 in [dp[j-k] for k in temp]:
            dp[j] = 1
        else:
            dp[j] = 0
    temp.append(nums[i])
    now = nums[i]
    dp[now] = 1

dp[temp[-1]] = 1
repeat = dp[temp[0]:temp[-1]+1]
lenrep = len(repeat)

result = 0
for i in range(temp[-1]+1, m+1):
    if 0 in [dp[i-k] for k in temp]:
        dp[i] = 1
    else:
        dp[i] = 0
    if i > temp[-1]+1 and repeat == dp[i-lenrep:i]:
        result = i
        break

for i in range(23,200,28):
    print(dp[i-28:i], i)
result = result-lenrep-temp[0]
loop = dp[temp[0]:result+temp[0]]
x = m//result
y = m%result
print(x*loop.count(0) + loop[:y].count(0) + temp[0]-1)