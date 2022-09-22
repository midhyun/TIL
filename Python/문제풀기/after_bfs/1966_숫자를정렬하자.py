import sys
sys.stdin = open('1966_숫자를정렬하자.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    nums = [*map(int, input().split())]
    nums.sort()
    print(f'#{test_case}', end=' ')
    for i in nums:
        print(i, end=' ')
    print()
