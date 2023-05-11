import sys
input = sys.stdin.readline

# 최대 예산사용을 위한 상한액정하기
N = int(input())
budgets = [*map(int, input().split())]
Total = int(input())
# 이분탐색
def binary_Search(budget, tot, n):
    lo = 1
    hi = tot

    if sum(budget) <= tot:
        return max(budget)

    while lo <= hi:
        mid = (lo + hi) // 2
        tmp = 0
        for city in budget:
            tmp += min(city, mid)

        if tmp <= tot:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

print(binary_Search(budgets, Total, N))