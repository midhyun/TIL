import sys
sys.stdin = open('4012_요리사.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input().split())

for test_case in range(1, T+1):
    