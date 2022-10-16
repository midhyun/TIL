import sys
sys.stdin = open('1039_교환.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
m = len(str(n))
print(n, k, m)