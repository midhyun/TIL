import sys
input = sys.stdin.readline
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
n_nums = [*map(int, input().split())]
M = int(input())
m_nums = [*map(int, input().split())]

answer = 1
for i in range(N):
    for j in range(M):
        gcd_result = gcd(n_nums[i], m_nums[j])
        answer *= gcd_result
        n_nums[i] //= gcd_result
        m_nums[j] //= gcd_result

print(str(answer)[-9:])