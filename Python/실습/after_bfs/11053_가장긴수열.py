import sys
sys.stdin = open('11053_가장긴수열.txt')
input = sys.stdin.readline
# 11053_가장 긴 증가하는 부분 수열
# 1 <= A <= 1000
# 시작지점을 1 ~ n 번째 까지. max > n 
A = int(input())
lst = list(map(int, input().split())) # [5 6 1 2 3]
dp = [0 for _ in range(A)]
for i in range(A):
    for j in range(i):
        if lst[j] < lst[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
            print(dp)
    dp[i] += 1
    print(dp)
print(max(dp))
