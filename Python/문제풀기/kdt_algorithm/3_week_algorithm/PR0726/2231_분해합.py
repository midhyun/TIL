## 가장 작은 생성자를 구해라.
# N의 분해합은 N과 N을 이루는 각 자리수의 합.
# 생성자가 없을경우 0을 출력.

N = int(input())
long = len(str(N))
if N < 20 :
    for ran in range(0,N):
        M = N - ran
        sum_m = sum(list(map(int, str(M))))
        if ran == sum_m: 
            print(M)
            break
    else: print('0')
else:
    for ran in range(long*10,0,-1):
        M = N - ran # 가장 작은 수는 N - 자릿수*10 이므로
        sum_m = sum(list(map(int, str(M))))
        if ran == sum_m: # 범위는 자릿수*10 하나씩 대조함
            print(M)
            break
    else: print('0')


        
    



