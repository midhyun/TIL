import sys
sys.stdin = open('2309.txt')
input = sys.stdin.readline

tall_lst = [int(input()) for _ in range(9)]
sum_ = sum(tall_lst)
n = len(tall_lst)

for i in range(n-1):
    if len(tall_lst) == 7:
        break
    for j in range(i+1, n):
        if sum_ - tall_lst[i] - tall_lst[j] == 100:
            tall_lst[i], tall_lst[j] = 0, 0
            for _ in range(2):
                tall_lst.remove(0)
            break
for i in sorted(tall_lst):
    print(i)