import sys
sys.stdin = open('1230_암호문3.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())
    origin_pw = [*map(int, input().split())]
    n_order = int(input())
    orders = input().strip().split()

    for i in range(len(orders)):
        if orders[i] == 'I':
            pos, cnt = int(orders[i+1]), int(orders[i+2])
            # print(orders[i], pos, cnt, i)
            origin_pw = origin_pw[:pos] + orders[i+3:i+3+cnt] + origin_pw[pos:]
        if orders[i] == 'D':
            pos, cnt = int(orders[i+1]), int(orders[i+2])
            origin_pw = origin_pw[:pos] + origin_pw[pos+cnt:]
        if orders[i] == 'A':
            cnt = int(orders[i+1])
            origin_pw += orders[i+2:i+2+cnt]

    print(f'#{test_case}',*origin_pw[:10])