def Rev(num):
    return num[::-1]                            # 입력받은 num 을 srt슬라이싱으로 뒤집기

X, Y = input().split()
print(int(Rev(str(int(Rev(X)) + int(Rev(Y)))))) # 뒤집은 숫자를 정수로 바꾸고 합 연산, 다시 문자열로바꾼후 뒤집고 정수로 바꿈.