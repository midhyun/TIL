import sys
input = sys.stdin.readline

W, N = map(int, input().split())
weights = [*map(int, input().split())]
dp = [False]*(W+1)

def solution():
    for i in range(1, N):
        for j in range(i+1, N):
            if weights[i] + weights[j] < W and dp[W-weights[i]-weights[j]]:
                return 'YES'
            
        for j in range(i):
            if weights[i] + weights[j] < W:
                dp[weights[i]+weights[j]] = True
    else:
        return 'NO'

print(solution())