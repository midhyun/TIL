import sys
sys.stdin = open('1860_진기의붕어빵.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n,m,k = map(int, input().split())
    stack = 0
    flag = True
    customer = sorted([*map(int,input().split())])
    for i in customer: # i => 손님이 도착한 시간
        stack += 1
        if (i//m)*k < stack:
            flag = False
            break
    if flag:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')