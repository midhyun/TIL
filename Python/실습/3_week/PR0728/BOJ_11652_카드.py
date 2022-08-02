import sys
sys.stdin = open('input.txt')

N = int(input())
card_dic = {}

for i in range(N):
    a = int(input())                                        # 카드숫자 입력
    card_dic[a] = card_dic.get(a , 0) + 1                   # 딕셔너리에 카드 추가 // 중복일 경우 숫자 카운트

lst = sorted(card_dic.items(), key= lambda x: (-x[1], x[0]))# 딕셔너리의 키-값쌍 뷰 생성, 값의 내림차순, 키의 오름차순 순서로 정렬 
print(lst[0][0])                                            # 가장 큰 값 중 오름차순 정렬된 키의 첫번째를 출력.