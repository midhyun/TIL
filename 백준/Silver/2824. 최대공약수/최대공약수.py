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

n_num = 1
m_num = 1
for num in n_nums:
    n_num *= num
for num in m_nums:
    m_num *= num

print(str(gcd(n_num, m_num))[-9:])