a, r, n = map(int,input().split())

for i in range(1,n):
    a *= r
    if i == n-1:
        print(a)