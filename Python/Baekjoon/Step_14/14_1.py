import sys
sys.stdin = open('14_1.txt')
input = sys.stdin.readline
# 배수와 약수_5086
# 4 x 3 = 12
# 1) 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 2) 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 3) 첫 번째 숫자가 두 번째 숫잔의 약수와 배수 모두 아니다.

while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')