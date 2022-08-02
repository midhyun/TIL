import sys
sys.stdin = open('input.txt')

lst = []
for i in range(5):
    score = sum(list(map(int, input().split())))
    lst.append(score)
print(lst.index(max(lst))+1, max(lst))
