import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
win_rate = (Y*100) // X

def binary_Search():
    Z = (Y*100) // X
    if Z >= 99:
        print(-1)
    else:
        answer = 0
        left = 1
        right = X
    
        while left <= right:
            mid = (left + right) // 2
            if (Y+mid)*100 // (X+mid) <= Z:
                left = mid+1
            else:
                answer = mid
                right = mid - 1
    
        print(answer)

if win_rate <= 99:
    binary_Search()
else:
    print(-1)