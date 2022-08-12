import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
moeum = 'aeiou'
for test_case in range(1, T+1):
    word = input()
    for spell in moeum:
        word = word.replace(spell,'')
    print(f'#{test_case} {word}')