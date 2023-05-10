import sys
import copy
from collections import deque
sys.stdin = open('2346_ 풍선터트리기.txt')
input = sys.stdin.readline


# sys.setrecursionlimit(int(1e5))

n = int(input())
arr = list(map(int, input().split()))
data = []

for i in range(1, n + 1):
    data.append((i, arr[i - 1]))

data = deque(data)

result = []

while True:
    index, step = data.popleft()
    result.append(index)

    # N개를 모두 꺼냈다면 종료
    if len(result) == n: break

    if step > 0:  # 오른쪽 회전
        for j in range(step - 1):
            right = data.pop()
            data.appendleft(right)
    else:  # 왼쪽 회전
        step *= -1
        for j in range(step):
            left = data.popleft()
            data.append(left)

for x in result:
    print(x, end=" ")
