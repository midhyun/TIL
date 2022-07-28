import sys
sys.stdin = open('input.txt')

N = int(input())                            # N 개의 카드
card_lst = input().split()                  # 카드의 리스트
M = int(input())                            # M 개의 찾을 숫자
find_lst = input().split()                  # 찾을 숫자 리스트
card_dict = {}

for i in card_lst:                          # 딕셔너리에 카드 갯수 카운트
    card_dict[i] = card_dict.get(i, 0) + 1

for i in find_lst:                          # 딕셔너리의 key(카드넘버)가 찾으려는 key(카드넘버)인 경우 카운트한 갯수 출력.
    print(card_dict.get(i, 0), end = ' ')
