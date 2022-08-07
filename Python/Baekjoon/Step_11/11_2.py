import heapq
import sys
sys.stdin = open('11_2.txt')
input = sys.stdin.readline
lst = []
N = int(input())
for i in range(N):
    lst.append(int(input()))
heapq.heapify(lst)
for j in range(N):
    print(heapq.heappop(lst))