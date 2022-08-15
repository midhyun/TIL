import sys
sys.stdin = open('14_8.txt')
input = sys.stdin.readline

# 다리놓기_1010
# 서쪽 N개, 동쪽 M개 (N < M)
# 경우의 수
# 다리 끼리 겹칠 수 없음.
# M 개에서 N개를 고르는 경우의 수, 부분집합
def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial(M-N)*factorial(N))
    print(result)