import sys
input = sys.stdin.readline

s, N, K, r1, r2, c1, c2 = map(int, input().split())
I = N**s

def check_b(I, x, y):
    if I == 1:
        return 0
    center = I//N

    if center * (N-K)//2 <= x < center * (N+K)//2 and center * (N-K)//2 <= y < center * (N+K)//2:
        return 1
    
    x %= center
    y %= center
    
    return check_b(I//N, x, y)

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(check_b(I, i, j), end="")
    print()