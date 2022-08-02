import sys
input = sys.stdin.readline
sys.stdin = open('input.txt')

num = int(input())
sta_j = []
sta_g = []
for i in range(num):
    sta_j.append(input())

for i in range(num-1):
    sta_g.append(input())
sta_j.sort()
sta_g.sort()

for i in range(num-1):
    if sta_j[i] != sta_g[i]:
        print(sta_j[i])
        break
else: print(sta_j[-1])
