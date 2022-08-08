import sys
sys.stdin = open('11170.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    str_ = ''
    for i in range(N, M+1):
        str_ += str(i)
    print(str_.count('0'))