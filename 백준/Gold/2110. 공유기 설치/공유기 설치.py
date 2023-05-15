import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()
lo, hi = 1, houses[N-1] - houses[0]

while lo <= hi:
    mid = (lo+hi)//2
    cnt = 1
    share = houses[0]

    for i in range(N):
        if houses[i] - share >= mid:
            cnt += 1
            share = houses[i]

    if cnt >= C:
        lo = mid + 1
    else:
        hi = mid - 1

if C == 2:
    print(houses[N-1] - houses[0])
else:
    print(hi)