import sys
sys.stdin = open('2436_공약수.txt')
input = sys.stdin.readline

def find_divisor(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num//i)
    divisors.sort()
    return divisors

A, B = map(int, input().split())
divisors = find_divisor(B)

def find_gcd(a, b):
    if a < b: a, b = b, a

    while True:
        remain = a % b
        if remain == 0:
            return b
        a, b = b, remain

sumDivisors = sys.maxsize
result = [0, 0]
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        # 두 수의 곱을 최대공약수로 나누면 최소공배수가 됨.
        if divisors[i]*divisors[j]//A == B:
            if A == find_gcd(divisors[i], divisors[j]) and sumDivisors > divisors[i]+divisors[j]:
                sumDivisors = divisors[i]+divisors[j]
                result[0], result[1] = divisors[i], divisors[j]

print(*result)