import sys
sys.stdin = open('2170_선긋기.txt')
input = sys.stdin.readline

n = int(input())
result = 0
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort()

temp = -int(1e9)
for s, e in lines:
    if s >= temp:
        result += abs(e-s)
    else:
        if e < temp: continue
        result += abs(e-temp)
    temp = e

print(result)