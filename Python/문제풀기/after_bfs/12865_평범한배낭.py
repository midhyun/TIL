import sys
sys.stdin = open('12865_평범한배낭.txt')
input = sys.stdin.readline

wv = [0]
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]    # 0 번째 row 0번째 col 있어야함.
for _ in range(n):
    w, v = map(int, input().split())
    wv.append((w, v))

for i in range(1, n+1):
    w, v = wv[i][0], wv[i][1]
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
print(dp[n][k])