import sys
sys.stdin = open('14_3.txt')
input = sys.stdin.readline
# 최소공배수_1934
# A, B 의 최소 공배수
# 유클리드 호제법
# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), 
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
T = int(input())
def gcd(m, n): # 최대 공약수,
    if m < n :
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

for test_case in range(1, T+1): # 최소 공배수 = A*B / 최대공약수
    A, B = map(int, input().split())
    gcd_ = gcd(A, B)
    print(int(A*B/gcd_))