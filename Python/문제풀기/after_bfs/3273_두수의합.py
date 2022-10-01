import sys
sys.stdin = open('3273_두수의합.txt')
input = sys.stdin.readline

n = int(input())
nums = [*map(int, input().split())]
x = int(input())
nums.sort()
cnt = 0
for i in range(n):
    for j in range(n,i,-1):
        if i+j < x:
            break
        if i+j == x:
            cnt += 1
            break