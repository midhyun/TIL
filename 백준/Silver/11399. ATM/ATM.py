import sys
input = sys.stdin.readline

n = int(input())
lst = sorted([*map(int, input().split())])

for i in range(1,n):
    lst[i] += lst[i-1]

print(sum(lst))