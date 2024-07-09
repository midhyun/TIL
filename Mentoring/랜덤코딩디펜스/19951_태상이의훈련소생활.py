import sys
sys.stdin = open('19951_태상이의훈련소생활.txt')
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    height = [*map(int, input().split())]
    # dp 배열을 N+2로 만들어서 dp[1:N+1]로 출력
    # dp[i]: i번째 에서 더해야할 높이
    dp = [0] * (N+2)
    # 조교의 명령 a ~ b 까지 k만큼 높이를 더함. b 이후는 더하지 않기 때문에 -k를 해줌
    for _ in range(M):
        a, b, k = map(int, input().split())
        dp[a] += k
        dp[b+1] -= k
    # 누적합으로 1 ~ N+1 까지의 높이를 구함
    for i in range(1, N+1):
        dp[i] += dp[i-1]
    # 기존 높이를 더해줌
    for i in range(1, N+1):
        dp[i] += height[i-1]
    print(*dp[1:N+1])

solution()
