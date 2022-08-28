import sys
sys.stdin = open('9251_LCS.txt')
input = sys.stdin.readline

a = list(input().strip())                           # a 문자열 리스트
b = list(input().strip())                           # b 문자열 리스트
dp = [[0]*1001 for _ in range(1001)]                # 문자열의 길이는 최대 1000개

for i in range(len(a)):                             # [ACAYKP]
    for j in range(len(b)):                         # [CAPCAK]
        if a[i] == b[j]:                            # a 문자열의 i번째 글자와 b문자열의 j번째 글자가 같을 때
            dp[i+1][j+1] = dp[i][j] + 1             # dp[i+1][j+1] = dp[i][j] + 1 [이전dp + 1]
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]) # 글자가 같지 않을 경우
                                                    # dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])  [i까지의 부분수열 중 가장 긴 공통 수열 길이]
print(dp[len(a)+1][len(b)+1])
