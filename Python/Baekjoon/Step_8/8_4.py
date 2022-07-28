# 소수 구하기
# 에라토스테네스의 체

M, n = map(int,input().split())


sieve = [True]*(n)                                    # n개의 불리언 리스트 생성.
sieve[1] = False
m = int(n ** 0.5)                                   # n의 최대 약수가 sqrt(n)이하 이므로 i = sqrt(n) 까지 검사
for i in range(2, m + 1):                           # 2부터 sqrt(n) 까지 순회
    if sieve[i] == True:                            # i번째 불리언이 참이면 하위 for문 순회
        for j in range(i+i, n, i):                  # i+1 부터 n까지 i의 배수들의 불리언 값을 False로 변경
            sieve[j] = False                        

for i in range(M, n):
    if sieve[i] == True:                            # 2부터 n까지 True인 값들을 리스트로 반환
        print(i)