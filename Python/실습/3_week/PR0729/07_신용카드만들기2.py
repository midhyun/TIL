from cgi import test
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    card_mk = False
    card_num = input().replace('-','')
    z = card_num[0]

    if len(card_num) == 16:
        if z == '3' or z == '4' or z == '5' or z == '6' or z == '9':
            card_mk = True
    print(f'#{test_case} {card_mk*1}')

