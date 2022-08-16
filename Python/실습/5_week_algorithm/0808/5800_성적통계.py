import sys
sys.stdin = open('5800.txt')

K = int(input())

for class_ in range(1, K+1):
    lst = sorted(list(map(int, input().split()))[1:],reverse=True)
    gap_lst = []
    for i in range(1,len(lst)):
        gap_lst.append(lst[i-1]-lst[i])
    print(f'Class {class_}')
    print(f'Max {max(lst)}, Min {min(lst)}, Largest gap {max(gap_lst)}')
