import sys
sys.stdin = open('11945.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n):
    a = input().strip()
    print(a[::-1])
