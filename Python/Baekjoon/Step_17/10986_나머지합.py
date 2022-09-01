import sys
sys.stdin = open('10986_나머지합.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [*map(int, input().split())]
psum = [0] *(n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1] + nums[i-1]

nums = list(map(lambda x: x % m,nums))
psum = list(map(lambda x: x % m, psum))
count = [0] * m
for p_sum in psum[1:]:
    count[p_sum] += 1
result = 0
for i in range(1, n+1):
    result += count[psum[i-1]]
    count[psum[i]] -= 1

print(result)