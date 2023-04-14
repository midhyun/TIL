import sys
sys.stdin = open('20300_서강근육맨.txt')
input = sys.stdin.readline

N = int(input())
loss = [*map(int, input().split())]
loss.sort()
tmp = 0
for i in range(N//2):
    tmp = max(loss[i] + loss[-i-2], tmp)
if N % 2 == 1:
    tmp = max(tmp, loss[N-1])

print(tmp)