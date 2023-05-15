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
    r1, c1 = stickers[i]
    sticker1 = r1*c1
    for j in range(i+1, N):
        r2, c2 = stickers[j]
        if ((r1 + r2) <= H and max(c1, c2) <= W) or (max(r1, r2) <= H and c1 + c2 <= W ):
            result = max(result, sticker1+(r2*c2))
        if ((r1 + c2) <= H and max(c1, r2) <= W) or (max(r1, c2) <= H and c1 + r2 <= W ):
            result = max(result, sticker1+(r2*c2))
        if ((c1 + r2) <= H and max(r1, c2) <= W) or (max(c1, r2) <= H and r1 + c2 <= W ):
            result = max(result, sticker1+(r2*c2))
        if ((c1 + c2) <= H and max(r1, r2) <= W) or (max(c1, c2) <= H and r1 + r2 <= W ):
            result = max(result, sticker1+(r2*c2))

print(result)