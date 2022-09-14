import sys
sys.stdin = open('11659_구간합.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]+[*map(int, input().split())]

for i in range(1, n+1):
    nums[i] += nums[i-1]

for i in range(m):
    x, y = map(int, input().split())
    print(nums[y]-nums[x-1])
