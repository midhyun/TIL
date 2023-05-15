import sys
sys.stdin = open('3079_입국심사.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
times = []
for _ in range(N):
    times.append(int(input()))

# 최소시간, 최대 걸리는 시간
lo, hi = 1, max(times)*M
# M이상의 사람을 검사할 수 있는 시간 hi 보다 lo가 커질 경우,
# hi가 최소시간으로 검사할 수 있는 시간.
while lo < hi:
    # 이분탐색을 위한 중간값
    mid = (lo + hi) // 2
    # 중간값의 시간동안 검사할 수 있는 사람의 수
    cnt = 0
    for time in times:
        cnt += mid // time
    # 사람의 수가 M보다 많이 검사 할 수 있다면 시간을 줄인다.
    if cnt >= M:
        hi = mid
    # 사람의 수가 M보다 적게 검사한다면 시간을 늘려준다.
    else:
        lo = mid + 1

print(hi)