import sys
sys.stdin = open('2217_로프.txt')
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

temp = ropes[0]*n
for i in range(1, n):
    tmp = ropes[i]*(n-i)
    if tmp > temp:
        temp = tmp

print(temp)