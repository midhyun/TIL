import sys
sys.stdin = open('5789_상자바꾸기.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n, q = map(int, input().split())
    boxes = [0] * (n + 1)
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            boxes[j] = i
    print(f'#{test_case}', end=' ')
    print(*boxes[1:])