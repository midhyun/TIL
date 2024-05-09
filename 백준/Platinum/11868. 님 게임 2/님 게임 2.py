import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    stones = list(map(int, input().split()))
    grundy = 0
    for stone in stones: grundy ^= stone
    print('koosaga' if grundy else 'cubelover')

solution()