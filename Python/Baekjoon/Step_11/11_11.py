import sys
import heapq
sys.stdin = open('11_11.txt')
input = sys.stdin.readline
N = int(input())

lst = list(map(int, input().split()))
lst_set = sorted(list(set(lst)))
lst_dic = {}
for i in range(len(lst_set)):
    lst_dic[lst_set[i]] = lst_dic.get(lst_set[i], i)
for i in lst:
    print(lst_dic[i], end=' ')