import sys
sys.stdin = open('1958_LCS3.txt')
input = sys.stdin.readline

# 알파벳 소문자, 최대 100글자
S1 = input().rstrip()
S2 = input().rstrip()
S3 = input().rstrip()
# dp[i][j][k] : 각 문자열에서 i, j, k 번째 문자 까지 최대LCS

def solution():
    dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
    for i in range(1, len(S1)+1):
        for j in range(1, len(S2)+1):
            for k in range(1, len(S3)+1):

                if S1[i-1] == S2[j-1] and S1[i-1] == S3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    return dp[len(S1)][len(S2)][len(S3)]

print(solution())