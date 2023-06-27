import sys
sys.stdin = open('19532_수학은비대면강의입니다.txt')
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
y = ((a*f) - (d*c))//((a*e) - (d*b))
if a == 0:
    x = (f-(e*y))//d
else:
    x = (c-(b*y))//a
print(x, y)