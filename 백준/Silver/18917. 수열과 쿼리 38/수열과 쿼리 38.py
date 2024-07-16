import sys
input = sys.stdin.readline

def solution():
    A = [0]
    M = int(input())
    sum_A = 0
    XOR_A = 0
    for _ in range(M):
        query = list(map(int, input().split()))
        if query[0] == 1:
            sum_A += query[1]
            XOR_A ^= query[1]
            A.append(query[1])
        elif query[0] == 2:
            sum_A -= query[1]
            XOR_A ^= query[1]
            A.pop()
        elif query[0] == 3:
            print(sum_A)
        elif query[0] == 4:
            print(XOR_A)

solution()
