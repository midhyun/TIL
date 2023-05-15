import sys
sys.stdin = open('2631_줄세우기.txt')
input = sys.stdin.readline

# N명의 아이들
N = int(input())
pos_child = []
for _ in range(N):
    pos_child.append(int(input()))

dp = [0]*(N)
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if pos_child[i] > pos_child[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))