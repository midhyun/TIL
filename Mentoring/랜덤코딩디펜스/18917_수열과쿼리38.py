import sys
sys.stdin = open('18917_수열과쿼리38.txt')
input = sys.stdin.readline

def solution():
    A = [0]
    M = int(input())
    sum_A = 0
    XOR_A = 0 # XOR_A = A[0] ^ A[1] ^ ... ^ A[n-1]
    for _ in range(M):
        query = list(map(int, input().split()))
        if query[0] == 1:
            sum_A += query[1]
            XOR_A ^= query[1]
            A.append(query[1])
        elif query[0] == 2:
            sum_A -= query[1]
            # XOR_A 에서 query[1]을 제거하는 방법은 XOR_A ^= query[1]을 사용하면 된다.
            # 이는 XOR_A = XOR_A ^ query[1]과 동일하다.
            XOR_A ^= query[1]
            A.pop()
        elif query[0] == 3:
            print(sum_A)
        elif query[0] == 4:
            print(XOR_A)
            
    return

solution()
