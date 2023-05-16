import sys
input = sys.stdin.readline

N = int(input())
files = sorted([*map(int, input().split())], reverse=True)

def binary_Search(x):
    lo = x + 1
    hi = N
    
    while lo < hi:
        mid = (lo + hi) // 2
        
        tmp = files[mid]/files[x]
        
        if tmp >= 0.9:
            lo = mid + 1
        else:
            hi = mid
    
    return lo - 1

result = 0
for i in range(N):
    result += binary_Search(i) - i

print(result)