n = int(input())

for i in range(n):
    m = list(map(int,input().split()))
    cnt = 0
    for j in m[1:]:
        if sum(m[1:])/m[0] < j :
            cnt += 1
    print(f'{cnt/m[0]*100:.3f}%')