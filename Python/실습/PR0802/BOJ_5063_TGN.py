import sys
sys.stdin = open('5063.txt')
input = sys.stdin.readline
N = int(input())

for test_case in range(1, N+1):
    r, e, c = map(int, input().split())     # 광고 x 수익 과 광고O - 광고비 수익 을 비교
    if r - (e-c) > 0:
        print('do not advertise')
    elif r - (e-c) < 0:
        print('advertise')
    elif r - (e-c) == 0:
        print('does not matter')