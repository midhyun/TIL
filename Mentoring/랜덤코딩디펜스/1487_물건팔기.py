import sys
sys.stdin = open('1487_물건팔기.txt')
input = sys.stdin.readline

def gain(cost):
    earn = 0
    for i in range(N):
        if info[i][0] >= cost:
            tmp = cost - info[i][1]
            if tmp > 0: earn += tmp
    return earn

N = int(input())
info = []
for _ in range(N):
    maxCost, dfee = map(int, input().split())
    info.append((maxCost, dfee))
info.sort()
result = 0
res = 0
for i in range(N):
    money = gain(info[i][0])
    if money > result:
        result = money
        res = info[i][0]

print(res)