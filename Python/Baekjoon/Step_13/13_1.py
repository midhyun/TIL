import sys
sys.stdin = open('13_1.txt')
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

if (w-x) > x:
    dx = x
else:
    dx = w-x
if (h-y) > y:
    dy = y
else:
    dy = h-y

if dx > dy:
    print(dy)
else:
    print(dx)