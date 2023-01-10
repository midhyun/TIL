import sys
sys.stdin = open('1931_회의실배정.txt')
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])
temp = 0
result = 0

for i, j in lst:
    if i >= temp:
        result += 1
        temp = j
print(result)