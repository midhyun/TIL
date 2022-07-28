import sys
sys.stdin = open('input.txt')

N = int(input())
card_dic = {}

for i in range(N):
    a = int(input())
    card_dic[a] = card_dic.get(a , 0) + 1

lst =[k for k,v in card_dic.items() if max(card_dic.values()) == v]
lst.sort()
print(lst[0])