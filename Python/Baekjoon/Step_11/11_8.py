import sys
import heapq
sys.stdin = open('11_8.txt')
input = sys.stdin.readline

lst = []
N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    heapq.heappush(lst, (y, x))

for _ in range(N):
    y, x = heapq.heappop(lst)
    print(x, y)