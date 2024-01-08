import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())

def solution(n, l, w, h):
    s, e = 0, min(l, w, h)
    for _ in range(100):
        mid = (s + e)/2
        if (l//mid)*(w//mid)*(h//mid) >= n:
            s = mid
        else:
            e = mid

    print(f'{e:0.10f}')

solution(N, L, W, H)