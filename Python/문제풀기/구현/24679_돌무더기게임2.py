import sys
sys.stdin = open('24679_돌무더기게임2.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    nums = sorted([*map(int, input().split())])
    front = nums[0]+nums[1]
    if front % 2 == 0:
        if front <= nums[2]:
            print('R')
        else:
            print('B')
    else:
        if front <= nums[2]:
            print('R')
        else:
            print('B')