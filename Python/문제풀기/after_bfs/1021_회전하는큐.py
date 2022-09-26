import sys
from collections import deque
sys.stdin = open('1021_회전하는큐.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [*map(int, input().split)]
