import sys
sys.stdin = open('20366_같이눈사람만들래.txt')
input = sys.stdin.readline
# 투 포인터
def solution():
    N = int(input())
    heights = list(map(int, input().split()))
    heights.sort()
    min_diff = sys.maxsize

    for i in range(N):
        for j in range(i+3, N):
            left, right = i+1, j-1
            while left < right:
                diff = heights[i] + heights[j] - heights[left] - heights[right]

                if abs(diff) < min_diff:
                    min_diff = abs(diff)

                if diff < 0: right -= 1
                else: left += 1
    
    print(min_diff)

solution()

# 가능한 눈사람 경우의 수를 모두 구해, 정렬후, 인접한 눈사람들의 차이를 비교 (같은 눈덩이를 사용하지 않는 조건 포함)
def solution2():
    N = int(input())
    heights = list(map(int, input().split()))
    min_diff = sys.maxsize

    snowmans = []
    for i in range(N-1):
        for j in range(1, N):
            snowmans.append([heights[i] + heights[j], i, j])
    snowmans.sort()

    for i in range(len(snowmans)-1):
        if min_diff > abs(snowmans[i][0] - snowmans[i+1][0]) and len(set(snowmans[i][1:]+snowmans[i+1][1:])) == 4:
            min_diff = abs(snowmans[i][0] - snowmans[i+1][0])
    print(min_diff)

# solution()