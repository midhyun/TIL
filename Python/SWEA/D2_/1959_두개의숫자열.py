import sys
from tkinter import N
sys.stdin = open('1959_두개의숫자열.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    lst_n = [*map(int, input().split())]
    lst_m = [*map(int, input().split())]
    if n >= m:
        n, m = m, n
        lst_n, lst_m = lst_m, lst_n
    result = []
    for i in range(m-n+1):
        sum = 0
        for j in range(n):
            sum += lst_n[j]*lst_m[j+i]
        result.append(sum)
    print(f'#{test_case} {max(result)}')