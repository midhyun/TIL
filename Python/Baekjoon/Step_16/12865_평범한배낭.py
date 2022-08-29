import sys
sys.stdin = open('12865_평범한배낭.txt')
input = sys.stdin.readline

n ,k = map(int, input().split())        # n개의 물건들 중 최대 k
wv = [(0,0)]
dp = [[0]*(k+1) for _ in range(n+1)]
for _ in range(n):
    w, v = map(int, input().split())    # w무게, v가치
    wv.append((w, v))
# 무게가 k 이하인 부분집합들 중에서 가치가 가장 큰값.
# 무게가 k 이하인 조합,

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = wv[i][0], wv[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
print(dp[n][k])