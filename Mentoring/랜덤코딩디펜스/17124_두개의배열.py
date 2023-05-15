import sys
sys.stdin = open('17124_두개의배열.txt')
input = sys.stdin.readline

def find_min(arr):
    cur = arr[2]
    lt = 2
    if arr[1] <= cur:
        cur = arr[1]
        lt = 1
    elif arr[0] <= cur:
        cur = arr[0]
        lt = 0

    return lt

def binary_Search(s, e, B, x):
    
    while s < e:
        diff = e - s
        if diff <= 1:
            return s
        
        mid = (s + e) // 2

        if x < B[mid] :
            e = mid
        else:
            s = mid

# 랜선자르기, 나무자르기 Low, high 중간점 mid ~
0 ,1, 2
# 0 ~ 2의 인덱스의 값 0 ~ 2 B = [8, 12, 16]  A 가 14일때

def solution():
    N, M = map(int, input().split())
    A = [*map(int, input().split())]
    B = sorted([*map(int, input().split())])
    c = 0
    for i in range(N):
        tmp = binary_Search(0, M-1, B, A[i])
        arr = []
        arr.append(abs(B[tmp-1] - A[i]))
        arr.append(abs(B[tmp] - A[i]))
        arr.append(abs(B[(tmp+1)%M] - A[i]))
        idx = find_min(arr)
        c += B[tmp + idx - 1]
    print(c)

T = int(input())
for _ in range(T):
    solution()