import sys
input = sys.stdin.readline

N = int(input())
loss = [*map(int, input().split())]
loss.sort()
tmp = 0


if N % 2 == 1:
    for i in range(N//2):
        tmp = max(loss[i] + loss[-i-2], tmp)
    tmp = max(tmp, loss[-1])
else:    
    for i in range(N//2):
        tmp = max(loss[i] + loss[-i-1], tmp)

print(tmp)