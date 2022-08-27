import sys
sys.stdin = open('1912_연속합.txt')
input = sys.stdin.readline

n = int(input())
lst = [*map(int, input().split())]
sum = [lst[0]]

for i in range(len(lst) -1):
    sum.append(max(sum[i] + lst[i+1], lst[i+1]))
print(max(sum))