import sys
sys.stdin = open('11694_님게임.txt')
input = sys.stdin.readline

def solution():
    N = int(input())
    stones = list(map(int, input().split()))
    grundy = 0
    for stone in stones: grundy ^= stone
    print('koosaga' if grundy else 'cubelover')

solution()