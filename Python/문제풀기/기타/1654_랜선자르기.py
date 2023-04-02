import sys
sys.stdin = open('1654_랜선자르기.txt')
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = []
for _ in range(K):
    lengths.append(int(input()))

