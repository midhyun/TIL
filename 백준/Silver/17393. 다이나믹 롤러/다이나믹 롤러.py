import sys
from bisect import bisect
input = sys.stdin.readline

def binary_Search(s, e):
    ink_ = ink_num[s]
    result = e
    while s < e:
        mid = (s + e) // 2

        if visco_num[mid] <= ink_:
            s = mid + 1
        else:
            e = mid

    return e


N = int(input())
ink_num = [*map(int, input().split())]
visco_num = [*map(int, input().split())]

for i in range(N):
    idx = bisect(visco_num, ink_num[i])
    print(idx - (i+1), end= ' ')