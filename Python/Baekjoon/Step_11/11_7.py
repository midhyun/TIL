import sys
import heapq
sys.stdin = open('11_7.txt')
input = sys.stdin.readline

lst = []
N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    heapq.heappush(lst, (x, y))

for _ in range(N):
    x, y = heapq.heappop(lst)
    print(x, y)