import sys
sys.stdin = open('1030_프렉탈평면.txt')
input = sys.stdin.readline

s, N, K, r1, r2, c1, c2 = map(int, input().split())
# s초후의 한 변의 길이
I = N**s

def check_b(line, x, y):
    if line == 1:
        return 0
    # 한 칸의 길이
    len_block = line//N
    # 해당 범위일 경우 검은칸이다.
    if len_block * (N-K)//2 <= x < len_block * (N+K)//2 and len_block * (N-K)//2 <= y < len_block * (N+K)//2:
        return 1
    
    x %= len_block
    y %= len_block

    return check_b(I//N, x, y)

# 문제에 주어진 범위만 흰/검 판별
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(check_b(I, i, j), end="")
    print()