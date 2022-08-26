import sys
sys.stdin = open('1912_연속합.txt')
input = sys.stdin.readline
# 시간초과 느낌인데 시간초과남
# 10, -4, 3, 1, 5, 6, -35, 21, -1
# 10!개 ? 팩토리얼개..?
# 범위를 줄여야되는데
# 양수면 다더하고 음수일때 확인? 이러면 dp아니잖아
n = int(input())
lst = [*map(int, input().split())]
results = []
result = 0
for i in range(n):
    if i != n:
        if lst[i] > 0:
            result += i
        elif abs(lst[i]) > result:
            results.append(result)
            result = 0
        else:
            result += i

if max(results) == 0:
    results.append(max(lst))

print(max(results))