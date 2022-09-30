import sys
sys.stdin = open('1016_제곱ss수.txt')
input = sys.stdin.readline


a, b = map(int, input().split())
check = [1]*(b-a+1)
for i in range(2, int(b**0.5)+1):
    t = i**2
    for j in range(a//t*t, b+1, t):
        if j-a >= 0 and check[j-a]:
            check[j-a] = 0
print(sum(check))