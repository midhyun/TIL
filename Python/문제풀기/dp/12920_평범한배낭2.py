import sys
sys.stdin = open('12920_평범한배낭2.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0]*(M+1)
obj = []
# 시간초과
# for i in range(1, N+1):
#     V, C, K = map(int, input().split())
#     for k in range(1, K+1):
#         for j in range(M+1):
#             dp[i][j] = max(dp[i][j], dp[i-1][j])
#             if j >= k*V:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j-(k*V)]+(C*k))

# K개의 물건을 2진법으로 조합을 줄임
# K = 5 , (1, 2, 2)
# K = 6 , (1, 2, 3) 으로 1 ~ 6을 조합 할 수 있음.
for i in range(1, N+1):
    V, C, K = map(int, input().split())

    i = 1
    while K > 0:
        cnt = min(i, K)
        obj.append((V*cnt, C*cnt))
        K -= i
        i *= 2

for V, C in obj:
    for i in range(M, V-1, -1):
        dp[i] = max(dp[i], dp[i - V] + C)

print(dp[M])
print(obj)