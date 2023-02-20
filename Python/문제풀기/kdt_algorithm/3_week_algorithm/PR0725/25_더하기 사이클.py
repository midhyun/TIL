# 0 <= N <= 99
N = int(input())
X = []
a = N # 초기 N값을 임시저장.
cnt = 0
while 1:
    X = (N//10), (N%10)
    Y = X[0]+X[1]
    N = (X[1]*10) + (Y%10)
    cnt += 1
    if N == a:
        break
print(cnt)