from xml.dom import NOT_SUPPORTED_ERR


import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = []
for i in range(N+M):
    lst.append(input())
no_see = lst[:N+1]
no_hear = lst[N+1:]

no_sh = {}
no_sh_lst = []
for i in no_see:
    no_sh[i] = no_sh.get(i, 0) + 1
for i in no_hear:
    no_sh[i] = no_sh.get(i, 0) + 1
    if no_sh[i] == 2:
        no_sh_lst.append(i)
print(len(no_sh_lst))
no_sh_lst.sort()
for i in no_sh_lst: 
    print(i)
