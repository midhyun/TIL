import sys
sys.stdin = open('2295_세수의합.txt')
input = sys.stdin.readline

N = int(input())
U = []
for _ in range(N):
    U.append(int(input()))
U.sort()

xyset = set()
for i in range(N):
    for j in range(N):
        xyset.add(U[i]+U[j])

zk = []
for k in range(N-1, -1, -1):
    for z in range(N):
        zk.append((U[k], U[k]-U[z]))

for k, xy in zk:
    if xy in xyset:
        print(k)
        break