import sys
sys.stdin = open('input.txt')

N = int(input())                                    # N 입력
sell_book = {}                                      # 팔린 책의 갯수 카운트 딕셔너리
lst = []                                            # 베스트 셀러 책.
for i in range(N):                                  # N개만큼 책 카운트
    book = input()
    sell_book[book] = sell_book.get(book, 0) +1     # 딕셔너리에 키 -값 생성후 1개씩 카운트
for i in sell_book:
    if sell_book[i] == max(sell_book.values()):     # 딕셔너리의 값 중 가장 큰값과 같은 값을 가진 키 == 최댓값의 키 들을 리스트에 추가
        lst.append(i)
lst.sort()
print(lst[0])                                       # 오름차순 정렬 후 가장 처음으로 오는 책을 출력.
