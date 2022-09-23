import sys
sys.stdin = open('1285_아름이의돌던지기.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    lst = [*map(abs, map(int, input().split()))]
    print(f'#{test_case} {lst.count(min(lst))}')