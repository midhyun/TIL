import sys
sys.stdin = open('9094_수학적호기심.txt')
input = sys.stdin.readline

def solution(n, m):
    cnt = 0
    for a in range(1, n+1):
        for b in range(a+1, n):
            if (a**2 + b**2 + m)%(a*b) == 0:
                cnt += 1
    return cnt
        
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    print(solution(n, m))