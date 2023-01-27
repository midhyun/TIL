import sys
sys.stdin = open('1026_보물.txt')
input = sys.stdin.readline

n = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

A.sort()
B.sort(reverse=True)

result = 0
for i in range(n):
    result += A[i]*B[i]

print(result)