import sys
sys.stdin = open('input.txt','r')

T = int(input())
for case in range(1,T+1):
    num = int(input())
    lst = list(map(int, input().split()))
    l_dict = {}
    for i in lst :
        l_dict[i] = l_dict.get(i,1) +1
    l_lst = []
    for j in range(1,101):
        if l_dict[j] == max(list(l_dict.values())):
            l_lst.append(j)
    print(f'#{case} {max(l_lst)}')