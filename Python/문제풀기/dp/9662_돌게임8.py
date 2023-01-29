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
# num[-1] 까지 DP 초기세팅
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
# DP만들기 1200개 까지
for i in range(temp[-1]+1, 1200):
    if 0 in [dp[i-k] for k in temp]:
        dp[i] = 1
    else:
        dp[i] = 0
# loop 찾기 (nums[-1]개 부터 600개의 루프길이 예상 )
for i in range(nums[-1],600):
    if dp[101:101+i] == dp[101+i:101+i+i]:
        loop = dp[101:101+i]
        break

x = ((m-100)//i)*(loop.count(0))
y = loop[:(m-100)%i].count(0)
z = dp[:101].count(0) - 1
result = x + y + z
print(result)