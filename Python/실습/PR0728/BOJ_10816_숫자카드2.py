import sys
sys.stdin = open('input.txt')

N = int(input())
card_lst = input().split()
M = int(input())
find_lst = input().split()
card_dict = {}

for i in card_lst:
    card_dict[i] = card_dict.get(i, 0) + 1

for i in find_lst:
    print(card_dict.get(i, 0), end = ' ')
