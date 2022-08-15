import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('14_7.txt')
input = sys.stdin.readline
N, K = map(int, input().split())
def facto(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def cal(n, k):
    return facto(n) // (facto(k)*facto(n-k))

print(cal(N, K)%10007)