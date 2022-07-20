# 손님 배정
# W개, H층
W, H = map(int, input().split())
Hotel = []
for i in range(H):
    for j in range(W):
        Hotel[i][j] = f'{i}{j}'
