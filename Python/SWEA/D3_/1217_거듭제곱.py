import sys
from tkinter import N
sys.stdin = open('1217_거듭제곱.txt')
input = sys.stdin.readline

def zegop(n, m, result):
    if m == 0:
        print(f'#{test_case} {result}')
        return
    x = result*n
    zegop(n,m-1,x)
for test_case in range(1, 11):
    n = int(input())
    n, m = map(int, input().split())
    zegop(n, m, 1)