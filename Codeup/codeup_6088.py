a, d, n = map(int,input().split())

for i in range(1,n):
    a += d
    if i == n-1:
        print(a)