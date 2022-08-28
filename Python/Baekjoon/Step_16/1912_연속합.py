import sys
sys.stdin = open('1912_연속합.txt')
input = sys.stdin.readline

n = int(input())
lst = [*map(int, input().split())]
sum = [lst[0]]

for i in range(len(lst) -1):
    sum.append(max(sum[i] + lst[i+1], lst[i+1]))
print(max(sum))

# 음수를 더해도 지금까지 더한 값이 양수라면, 계속 더하는게 이득
# 음수를 더했는데, 지금까지 더한 값이 음수라면, 버리고 새로 더하는게 이득
