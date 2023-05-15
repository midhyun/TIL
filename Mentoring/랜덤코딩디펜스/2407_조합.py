import sys
sys.stdin = open('2407_조합.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
result = 1
for i in range(N-M+1, N+1):
    result *= i
for i in range(1, M+1):
    result //= i
print(result)