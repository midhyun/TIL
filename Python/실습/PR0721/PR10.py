# 우영우..
# 문자열 인덱싱
import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    woo = str(input())
    print(f'#{test_case} {(woo[:] == woo[::-1])*1}')