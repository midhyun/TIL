import sys
sys.stdin = open('3142_영준이와신비한뿔의숲.txt')
input = sys.stdin.readline

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    twin = n-m
    unicorn = m-twin
    print(f'#{test_case}', unicorn, twin)
