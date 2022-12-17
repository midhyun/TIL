import sys
from collections import deque
sys.stdin = open('15730_수영장사장님.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [map(int, input().split()) for _ in range(n)]
