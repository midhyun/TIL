import sys
sys.stdin = open('2616_소형기관차.txt')
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
T = int(input())
# dp[i][j] = i번 열차로 j번위치 까지의 최댓값
dp = [[0]*(N+1) for _ in range(3)]
# 누적합
for i in range(1, N):
    nums[i] += nums[i-1]

nums = [0] + nums
# i번째 위치까지 첫번째 소형 열차로 끌었을때 최댓값
for i in range(1, N+1):
    start = max(0, i-T)
    dp[0][i] = max(dp[0][i-1], nums[i] - nums[start])
dp[0][0] = nums[0]
# i번째 소형열차로 j위치에서 끌었을때 최댓 값
for i in range(1, 3):
    for j in range(T*(i+1), N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-T] + (nums[j] - nums[j-T]))

print(dp[2][N])

for d in dp:
    print(d)