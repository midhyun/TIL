import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    sent = input()
    sent = sent.replace('d','a')
    sent = sent.replace('b','d')
    sent = sent.replace('a','b')
    sent = sent.replace('p','a')
    sent = sent.replace('q','p')
    sent = sent.replace('a','q')
    sent_mir = sent[::-1]
    print(f'#{test_case} {sent_mir}')