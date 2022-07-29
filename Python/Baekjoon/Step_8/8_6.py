# 골드바흐의 추측
# 2보다 큰 모든 짝수는 **두 소수**의 합으로 나타낼 수 있다는 것이다.
# 파티션이 여러개인 경우 두 소수의 차이가 작은 것으로.
import sys
sys.stdin = open('input.txt')

T = int(input())
n_lst = []

for test_case in range(1, T+1):
    n_lst.append(int(input()))
num = max(n_lst)
prime_lst = [False,False] + [True]*(num - 1)

m = int((num)**0.5)
for i in range(2, m+1):
    if prime_lst[i] == True:
        for j in range(i+i, num + 1, i):
            prime_lst[j] = False

cnt = 0
for i in n_lst:
    for j in range(i//2, 0, -1):
        if prime_lst[j] == True:
            k = i - j
            if prime_lst[k] == True:
                cnt += 1
                print(f'{j} {k}')
                break