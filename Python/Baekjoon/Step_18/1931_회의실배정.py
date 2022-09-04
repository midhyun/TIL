import sys
sys.stdin = open('1931_회의실배정.txt')
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    start, end = map(int,input().split())
    lst.append([start, end])
lst = sorted(lst, key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])

last = 0
cnt = 0
for i,j in lst:
    if i >= last:
        cnt += 1
        last = j
print(cnt)