import sys
sys.stdin = open('5948_새샘이의735.txt')
input = sys.stdin.readline
from itertools import combinations

t = int(input())
for test_case in range(1, t+1):
    nums = map(int, input().split())
    combies = list(combinations(nums,3))
    combies = list(set([*map(sum, combies)]))
    combies.sort()

    print(f'#{test_case}', combies[-5])