import sys
sys.stdin = open('16922_로마숫자만들기.txt')
input = sys.stdin.readline

N = int(input())
check = [[0]*(50*N+1) for _ in range(N)]
check[0][1], check[0][5], check[0][10], check[0][50] = 1, 1, 1, 1

# i개의 문자를 사용해서 j의 숫자를 만들수 있는경우.
for i in range(1, N):
    for j in range(50*N+1):
        # 가능한 모든 조합
        if check[i-1][j]:
            check[i][j+1] = 1
            check[i][j+5] = 1
            check[i][j+10] = 1
            check[i][j+50] = 1

# 최종 N개의 문자를 사용해서 만들수 있는 숫자의 갯수
print(sum(check[N-1]))