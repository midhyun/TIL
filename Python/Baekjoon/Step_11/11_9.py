import sys
import heapq
sys.stdin = open('11_9.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    a = input().strip()
    lst.append((len(a), a))
lst = list(set(lst))
lst.sort(key = lambda x : (x[0], x[1]))

for i in lst:
    print(i[1])