import sys
sys.stdin = open('1453.txt')

N = int(input())
lst = [*map(int, input().split())]
check = set()
cnt = 0
for i in lst:
    if i not in check:
        check.add(i)
    elif i in check:
        cnt += 1
print(cnt)