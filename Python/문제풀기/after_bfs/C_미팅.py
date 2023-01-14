import sys
sys.stdin = open('C_미팅.txt')
input = sys.stdin.readline

n, m, c = map(int, input().split())
satisfied = [[*map(int, input().split())] for _ in range(c)]
char_a = [*map(int,input().split())]
char_b = [*map(int,input().split())]

for i in range(n):
    char_a[i] -= 1
for i in range(m):
    char_b[i] -= 1

dp = [[0] *(m) for _ in range(n)]
dp[0][0] = satisfied[char_a[0]][char_b[0]]
for j in range(1, m):
    dp[0][j] = max(dp[0][j-1], satisfied[char_a[0]][char_b[j]])
for i in range(n):
    dp[i][0] = [satisfied[char_a[i]][char_b[0]], i, 0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j-1] + satisfied[char_a[i]][char_b[j]], dp[i-1][j], dp[i][j-1])
print(dp)