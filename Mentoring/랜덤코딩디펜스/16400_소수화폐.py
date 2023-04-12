import sys
sys.stdin = open('16400_소수화폐.txt')
input = sys.stdin.readline

N = int(input())
check = [False]*(N+1)
nums = []
check[1] = True
for i in range(2, N+1):
    if not check[i]:
        check[i] = True
        nums.append(i)
        for j in range(i, N+1, i):
            check[j] = True

dp = [0]*(N+1)
for i in range(len(nums)):
    dp[nums[i]] += 1
    for j in range(nums[i], N+1):
        dp[j] += dp[j-nums[i]]
        dp[j] %= 123456789

print(dp[-1])