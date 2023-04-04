import sys
sys.stdin = open('1654_랜선자르기.txt')
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = []
for _ in range(K):
    lengths.append(int(input()))
# start : 시작변수, end : 끝변수
start = 1
end = max(lengths)
# end가 start 보다 작아지면 종료.
while start <= end:
    print(start, end)
    # 시작변수와 끝변수의 중간 값
    mid = (start + end) // 2
    # 랜선의 갯수
    cnt = 0
    # 기존 랜선들을 mid 길이 만큼 잘랐을 때 랜선의 갯수
    for i in range(K):
        cnt += lengths[i] // mid
    # 자른 랜선의 갯수가 N이상이면 mid보다 크게 잘라야 함
    if cnt >= N:
        start = mid + 1
    # 랜선의 갯수가 N이하이면 mid보다 작게 잘라야 함
    else:
        end = mid - 1
print(end)

# 이분탐색
# 이분 탐색은 off-by-one error가 발생하기 쉬워서 늘 헷갈립니다.
# 이분 탐색 문제를 풀다보면 탈출 조건으로 lo <= hi, lo < hi, lo + 1 < hi 중 어느 걸 선택해야 할 지,
# 정답이 lo인지 hi인지 (lo + hi) / 2인지 모르겠고, 심지어는 while문이 끝나지 않아서 시간초과를 받기도 합니다.