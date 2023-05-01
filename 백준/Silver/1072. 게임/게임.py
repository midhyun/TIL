import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
win_rate = (Y*100) // X

def binary_Search():
    lo = 1
    hi = X
    answer = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        if (Y+mid)*100 // (X+mid) <= win_rate:
            lo = mid + 1
        else:
            answer = mid
            hi = mid - 1 
    
    print(answer)

if win_rate < 99:
    binary_Search()
else:
    print(-1)