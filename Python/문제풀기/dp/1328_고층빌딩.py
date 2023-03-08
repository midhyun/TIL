import sys
sys.stdin = open('1328_고층빌딩.txt')
input = sys.stdin.readline

N, L, R = map(int, input().split())
num = 1000000007
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = 1
# i개의 건물, 왼쪽에서 j개, 오른쪽에서 k개
# = 맨왼쪽에 추가(j-1, k) + 맨오른쪽에 추가(j, k-1) + 사이에 추가(j, k) *(i-2)
for i in range(2, N+1):
    for j in range(1, L+1):
        for k in range(1, R+1):
            dp[i][j][k] = (dp[i-1][j-1][k] + dp[i-1][j][k-1]
                           + dp[i-1][j][k]*(i-2)) % num

print(dp[N][L][R])