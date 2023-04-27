import sys
sys.stdin = open('16937_두스티커.txt')
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = []
for _ in range(N):
    a, b = map(int, input().split())
    stickers.append((a, b))

result = 0

for i in range(N):
    r = H - stickers[i][0]
    c = W - stickers[i][0]
    sticker1 = (stickers[i][0]*stickers[i][1])
    for j in range(i+1, N):
        if (r - stickers[j][0]) >= 0 and (stickers[j][1] <= W):
            result = max(result, sticker1+(stickers[j][0]*stickers[j][1]))
        elif (r - stickers[j][1]) >= 0 and (stickers[j][0]) <= H:
            result = max(result, sticker1+(stickers[j][0]*stickers[j][1]))

    for j in range(i+1, N):
        if (c - stickers[j][0]) >= 0 and (stickers[j][1] <= H):
            result = max(result, sticker1+(stickers[j][0]*stickers[j][1]))
        elif (c - stickers[j][1]) >= 0 and (stickers[j][0]) <= W:
            result = max(result, sticker1+(stickers[j][0]*stickers[j][1]))

print(result)