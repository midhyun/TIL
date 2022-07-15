x = int(input())
y = input()
y = list(y)
d = y.reverse() # y.revers() 명령어 자체는 y 리스트의 순서를 바꾸어서 입력해주기 때문에 d = none 값이 됩니다.
d = list((int,d)) # d = none 인 상태에서 정수형으로 변환하고 리스트에 class int와 None을 넣어주는 결과가 됩니다.
print(y)
