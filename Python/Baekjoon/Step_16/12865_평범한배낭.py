import sys
sys.stdin = open('12865_평범한배낭.txt')
input = sys.stdin.readline

n ,k = map(int, input().split())        # n개의 물건들 중 최대 k
wv = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    w, v = map(int, input().split())    # w무게, v가치
    wv.append((w, v))

for i in range(n):                      # 
    for j in range(n):
