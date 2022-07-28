import sys
sys.stdin = open('input.txt')

N = int(input())
sell_book = {}
lst = []
for i in range(N):
    book = input()
    sell_book[book] = sell_book.get(book, 0) +1
for i in sell_book:
    if sell_book[i] == max(sell_book.values()):
        lst.append(i)
lst.sort()
print(lst[0])
