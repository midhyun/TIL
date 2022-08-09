import sys
sys.stdin = open('2587.txt')
input = sys.stdin.readline

num_lst = [int(input()) for _ in range(5)]
num_lst.sort()

print(sum(num_lst)//len(num_lst))           # 평균
print(num_lst[len(num_lst)//2])             # 중앙값