import sys
sys.stdin = open('1264.txt')
input = sys.stdin.readline

moeum = {'a','e','i','o','u'}                       # 모음 리스트
while True:
    sen = input().strip().lower()                   # 문장을 변수에 담아줌().개행제거().소문자변환()
    if sen == '#':                                  # '#' 을 입력 받을 경우 반복문 종료
        break
    cnt = 0
    for i in sen:                                   # 문장에서 모음의 개수를 셈
        if i in moeum:
            cnt += 1
    print(cnt)