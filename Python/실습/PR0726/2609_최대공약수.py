import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

def prime(num): # 인수분해 
    insu = 2
    lst = [] # 인수분해한 리스트 [ ]
    while num != 1:
        if num % insu == 0:
            num /= insu
            lst.append(insu)      
            continue
        else : insu += 1 
    insu = {}  
    for i in lst: # 인수 하나씩 꺼내서 딕셔너리에 넣자
        insu[i] = insu.get(i, 0) + 1
    return insu # [2, 2, 2, 3, 3]  ==>  [2^3, 3^2] = > {2:3, 3:2}



A = prime(A) # 인수분해 딕셔너리 {} 24,
B = prime(B) # 18
insus = list(set(A)) # [2, 3] [2,2,2,3,3,]
insus.extend(list(set(B))) # [2, 3] or [5, 7]

max_ = 1 # 최대 공약수  
for key in list(set(insus)): # [2, 3] 최대 공약수 = 공통된 인수 중 작은지수의 인수들을 곱한 값
    if not key in A:        # 5^0 = 1, 7^0 = 1
        max_ *= 1
    elif not key in B: 
        max_ *= 1
    elif A[key] <= B[key]:        # 지수의 작은값끼리 곱해줌, => 최대공약수
        max_ *= (key**A[key])
    elif B[key] <= A[key]:
        max_ *= (key**B[key])
print(max_)

min_ = 1   # 최소 공배수
for key in list(set(insus)):

    if not key in B:            
        min_ *= key**A[key]
    elif not key in A:
        min_ *= key**B[key]            
    elif A[key] <= B[key]:        # 각 인수의 제곱항의 큰 값끼리 곱해줌, => 최소공배수
        min_ *= (key**B[key])
    elif B[key] <= A[key]:
        min_ *= (key**A[key])       
print(min_)