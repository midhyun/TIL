import sys
import heapq
sys.stdin = open('11_4.txt')
input = sys.stdin.readline

N, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
print(lst[k-1])
