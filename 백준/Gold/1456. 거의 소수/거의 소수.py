import sys
input = sys.stdin.readline
# 어떤 수가 소수의 N제곱 꼴일 때, 그 수를 거의 소수라고 함.

def find_prime():
    for i in range(2, m):
        if not check[i]:
            prime.append(i)
            for j in range(i+i, m, i):
                check[j] = True

def like_prime(x):
    cnt = 0
    cur = x*x
    while cur <= B:
        if cur >= A:
            cnt += 1
        cur *= x
    return cnt

A, B = map(int, input().split())
prime = []
m = int(B**0.5) + 1
check = [False]*(m + 3)

find_prime()

res = 0
for p in prime:
    res += like_prime(p)

print(res)