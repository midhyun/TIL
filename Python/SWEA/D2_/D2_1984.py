import sys
sys.stdin = open('D2_1984.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    nums = [*map(int, input().strip().split())]
    avg_ = sum(nums) - min(nums) - max(nums)
    print(f'#{test_case} {round(avg_/8)}')