import sys
sys.stdin = open('1228_암호문1.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n_pw = int(input())
    origin_pw = input().strip().split()
    n_order = int(input())
    orders = input().strip().split('I')
    for i in range(1,n_order+1):
        order = orders[i].split()
        origin_pw = origin_pw[:int(order[0])] + order[2:] + origin_pw[int(order[0]):]
    print(f'#{test_case}',*origin_pw[:10])