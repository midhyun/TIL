import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('14_6.txt')
input = sys.stdin.readline
N, K = map(int, input().split())
def facto(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def cal(n, k):
    return facto(n) / (facto(k)*facto(n-k))

print(int(cal(N, K)))

# def facto(n):
#     if n == 1:
#         return 1
#     else:
#         return n*facto(n-1)

# result = facto(N) / (facto(K)*facto(N-K))
# print(int(result))
