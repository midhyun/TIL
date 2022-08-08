import sys
import heapq
sys.stdin = open('11_10.txt')
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    age, name = input().split()
    lst.append((int(age), i, name))
lst.sort(key = lambda x: (x[0], x[1]))

for i in lst:
    print(i[0], i[2])