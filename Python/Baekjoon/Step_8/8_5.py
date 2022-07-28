# 베르트랑 공준
# n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다
while True:
    n = int(input())
    if n == 0:
        break
    # 에라토스테네스의 체       
    prime = [True] * ((2 * n) + 1)               # 2*n 까지의 소수를 찾는다.
    m = int((2*n)**0.5)                          # True인 인덱스값 == 소수
    for i in range(2, m + 1):
        if prime[i] == True:
            for j in range(i + i, 2 * n + 1, i):
                prime[j] = False
    lst = []
    for i in range(n+1, (2 * n) + 1):            # n+1 부터 2*n 까지의 소수를 리스트에 추가한다.
        if prime[i] == True:
            lst.append(i)
    print(len(lst))
