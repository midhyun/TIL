import sys
sys.stdin = open('11057_오르막수.txt')
input = sys.stdin.readline

n = int(input())

lst = [[1]*10 for _ in range(n+1)]

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            lst[i][j] = sum(lst[i-1]) % 10007
        else:
            lst[i][j] = (lst[i][j-1] - lst[i-1][j-1]) %10007

print(sum(lst[n])%10007)
