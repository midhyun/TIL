N = int(input())

for i in range(1,N+1):
    cnt = 0
    j = str(i)
    for k in j:
        if k == '3':
            cnt += 1
        elif k == '6':
            cnt += 1
        elif k == '9':
            cnt += 1
    if cnt != 0:
        print('-'*cnt,end=' ')
    else : print(i,end=' ')
    