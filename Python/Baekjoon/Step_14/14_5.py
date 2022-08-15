import sys
sys.stdin = open('14_5.txt')
input = sys.stdin.readline

N = int(input())
rings = list(map(int, input().split()))
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(1,N):
    gcd_ = gcd(rings[0], rings[i])
    print(f'{int(rings[0]/gcd_)}/{int(rings[i]/gcd_)}')