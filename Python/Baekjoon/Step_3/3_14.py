N = int(input())
M = N
cnt = 0
while 1 :    
    X = (M//10), (M%10)
    Y = X[0]+ X[1]
    M = (X[1]*10)+(Y%10)
    cnt += 1
    if M == N :
        break
print(cnt)