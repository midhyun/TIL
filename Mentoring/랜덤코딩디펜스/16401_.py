import sys
sys.stdin = open('16401_.txt')
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    snacks = sorted([*map(int, input().split())])
    left, right = 0, snacks[-1] + 1
    
    def check(n):
        count = 0
        for snack in snacks:
            count += snack // n
        return count >= M 

    while left + 1 < right:
        mid = (left + right) // 2

        if (check(mid)): left = mid
        else: right = mid

    print(left)
solution()