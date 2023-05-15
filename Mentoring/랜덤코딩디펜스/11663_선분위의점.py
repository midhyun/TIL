import sys
sys.stdin = open('11663_선분위의점.txt')
input = sys.stdin.readline

def min_dot(mn):
    lo = 0
    hi = N-1
    while lo <= hi:
        mid = (lo + hi) // 2

        if dots[mid] < mn:
            lo = mid + 1
        else:
            hi = mid - 1
        
    return hi + 1

def max_dot(mx):
    lo = 0
    hi = N-1
    while lo <= hi:
        mid = (lo + hi) // 2

        if dots[mid] > mx:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi

N, M = map(int, input().split())
dots = [*map(int, input().split())]
dots.sort()

for _ in range(M):
    s, e = map(int, input().split())
    print(max_dot(e) - min_dot(s) + 1)

