N = int(input())
I = list(map(int, input().split()))
sml = I[0]
bg = I[0]
for i in range(N):
    if sml >= I[i]:
        sml = I[i]
for i in range(N):
    if bg <= I[i]:
        bg = I[i]
print(sml,bg)