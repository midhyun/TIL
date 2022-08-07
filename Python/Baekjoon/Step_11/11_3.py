import heapq
import sys
sys.stdin = open('11_3.txt')
input = sys.stdin.readline
lst = [0]*10001
N = int(input())
for i in range(N):
    a = int(input())
    lst[a] += 1
for j in range(10001):
    if lst[j] != 0:
        for _ in range(lst[j]):
            print(j)