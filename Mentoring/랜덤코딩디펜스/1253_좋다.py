import sys
from collections import defaultdict
sys.stdin = open('1253_좋다.txt')
input = sys.stdin.readline

def solution():
    N = int(input())
    arr = [*map(int, input().split())]
    arr.sort()
    cnt = 0
    for i in range(N):
        s, e = 0, N-1
        while s < e:
            sum = arr[s] + arr[e]
            if sum == arr[i]:
                if s == i:
                    s += 1
                elif e == i:
                    e -= 1
                else:
                    cnt += 1 
                    break
            elif sum > arr[i]:
                e -= 1
            else: s += 1
    print(cnt)

solution()