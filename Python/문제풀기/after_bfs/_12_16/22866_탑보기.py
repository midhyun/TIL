import sys
sys.stdin = open("22866_탑보기.txt")
input = sys.stdin.readline

n = int(input())
height = [*map(int, input().split())]

stack = []
cnt = [0] * (n+1)
near = [[int(1e9), int(1e9)] for _ in range(n+1)]

lst = [1,2,3,4,5]

for idx, v in enumerate(height, start=1):
    while stack and stack[-1][1] <= v :
        stack.pop()
    cnt[idx] += len(stack)
    if stack:
        dist = abs(stack[-1][0] - idx)
        if dist < near[idx][1]:
            near[idx][1] = dist
        elif dist == near[idx][1] and stack[-1][0] < near[idx][0]:
            near[idx][0] = stack[-1][0]
    stack.append((idx, v))

stack = []
for idx, v in reversed(list(enumerate(height, start=1))):
    while stack and stack[-1][1] <= v:
        stack.pop()
    cnt[idx] += len(stack)
    if stack:
        dist = abs(stack[-1][0] - idx)
        if dist < near[idx][0]:
            near[idx][0] = dist
            near[idx][1] = stack[-1][0]
        elif dist == near[idx][0] and stack[-1][0] < near[idx][1]:
            near[idx][1] = stack[-1][0]
    stack.append((idx, v))

for i in range(1, n+1):
    if cnt[i] > 0:
        print(cnt[i], near[i][1])
    else:
        print(0)