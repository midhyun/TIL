import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
MX_A = max(A)
check = [False]*(MX_A+1)

def prime(x):

    for i in range(2, x+1):
        if not check[i]:
            for j in range(i+i, x+1, i):
                if not check[j]: check[j] = True

prime(MX_A)
primes = set()
for num in A:
    if not check[num]:
        primes.add(num)

if not primes:
    print(-1)
else:
    result = 1
    for num in primes:
        result *= num
    print(result)