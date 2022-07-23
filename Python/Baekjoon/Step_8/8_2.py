M = int(input())
N = int(input())
lst = []

for i in range(M,N+1):
    sosu = True
    if 2 > i:
        sosu = False
    for j in range(i-1,1,-1):
        if i % j == 0:
            sosu = False
    
    if sosu == True:
        lst.append(i)


if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))