import sys
sys.stdin = open('9184_신나는함수.txt')
input = sys.stdin.readline

# 셋중 하나라도 0이하일 경우 1
# 셋중 하나라도 20초과일 경우 w(20,20,20)
# a < b < c 일 경우 w(a,b,c-1) + w(a,b-1,c-1) - w(a, b-1, c)
# 그 외의 경우  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) 

dp = [[[0]*51 for _ in range(51)] for _ in range(51)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b ,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
