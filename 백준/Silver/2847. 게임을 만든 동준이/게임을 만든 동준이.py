import sys
input = sys.stdin.readline

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))

temp = scores[-1]
result = 0
for i in range(n-2, -1, -1):
    if scores[i] >= temp:
        diff = scores[i] - temp + 1
        result += diff
        scores[i] -= diff
    temp = scores[i]
print(result)