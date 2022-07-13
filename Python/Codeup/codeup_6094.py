n = int(input())
a = list(map(int,input().split()))
min_num = a[0]

for i in range(n):
    if min_num >= a[i] :
        min_num = a[i]
print(min_num)