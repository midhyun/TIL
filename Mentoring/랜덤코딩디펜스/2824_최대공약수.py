import sys
sys.stdin = open('2824_최대공약수.txt')
input = sys.stdin.readline
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
n_nums = [*map(int, input().split())]
M = int(input())
m_nums = [*map(int, input().split())]

# answer = 1
# for i in range(N):
#     for j in range(M):
#         gcd_result = gcd(n_nums[i], m_nums[j])
#         answer *= gcd_result
#         n_nums[i] //= gcd_result
#         m_nums[j] //= gcd_result

# print(str(answer)[-9:])

n_num = 1
m_num = 1
for num in n_nums:
    n_num *= num
for num in m_nums:
    m_num *= num

print(str(gcd(n_num, m_num))[-9:])