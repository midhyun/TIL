import sys
sys.stdin = open('26093_고양이목에리본.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
satis = []
for i in range(N):
    temp = [*map(int, input().split())]
    satis.append(temp)

dp = [[0]*K for _ in range(N)]
dp[0] = satis[0]
temp = sorted(dp[0])

for i in range(1, N):
    tmp = (temp[-1], temp[-2])
    for j in range(K):
        if dp[i-1][j] == tmp[0]:
            dp[i][j] = satis[i][j] + tmp[1]
        else:
            dp[i][j] = satis[i][j] + tmp[0]
    temp = sorted(dp[i])

print(max(dp[-1]))