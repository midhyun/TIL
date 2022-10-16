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
    w, v = wv[i][0], wv[i][1]                               # i번 물건의 무게와 가치
    for j in range(1, k+1):                                 # 1 ~ k 까지의 최대무게일 경우 가치의 최대값
        if j < w:                                           # 현재 물건의 무게가 현재 최대 담을 수 있는 무게보다 크다면
            dp[i][j] = dp[i-1][j]                           # dp는 이전줄을 가져옴
        else:                                               # 그 외의 경우라면
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])    # dp는 현재 무게의 물건을 넣었을 때 가치의 최대 값과 이전물건까지 현재무게의 최대 값중 큰 값
print(dp[n][k])                                             # 마지막 물건까지 넣어 보았을 때 최대 무게 최대 가치의 값