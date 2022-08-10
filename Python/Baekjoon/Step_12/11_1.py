import sys
sys.stdin = open('11_1.txt')
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
cards_find = list(map(int, input().split()))

for card in cards_find:
    if card in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')