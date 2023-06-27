import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
y = ((a*f) - (d*c))//((a*e) - (d*b))
if a == 0:
    x = (f-(e*y))//d
else:
    x = (c-(b*y))//a
print(x, y)