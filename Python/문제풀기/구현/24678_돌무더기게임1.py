import sys
sys.stdin = open('24678_돌무더기게임1.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    nums = [*map(int, input().split())]
    cnt = 0
    for num in nums:
        if num % 2 == 1:
            cnt += 1
    if cnt < 2:
        print('R')
    else:
        print('B')