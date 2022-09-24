import sys
sys.stdin = open('1970_쉬운거스름돈.txt')
input = sys.stdin.readline


t = int(input())
for test_case in range(1, t+1):
    money = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
    n = int(input())
    for k in money.keys():
        if n >= k:
            money[k] = n//k
            n = n%k
    print(f'#{test_case}')
    for v in money.values():
        print(v, end=' ')
    print()