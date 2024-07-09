import sys
sys.stdin = open('3020_개똥벌레.txt')
input = sys.stdin.readline

def solution():
    N, H = map(int, input().split())
    dp = [0]*(H+2)
    for i in range(N):
        h = int(input())
        # 1에서부터 h까지 부숴야 하므로 1추가 h이후는 없으므로 다시 -= 1
        if i % 2 == 0:
            dp[1] += 1
            dp[h+1] -= 1
        # 1에서부터 h-1까지 없으므로 더하지않고 h부터 더해줌
        else:
            dp[H-h+1] += 1
    # 누적합
    for i in range(1, H+1):
        dp[i] += dp[i-1]
    dp = dp[1:H+1]
    # 최소값과 최소값의 개수
    min_value = min(dp)
    cnt = dp.count(min_value)
    print(min_value, cnt)

solution()
