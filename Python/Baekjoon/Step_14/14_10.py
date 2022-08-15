import sys
sys.stdin = open('14_10.txt')
input = sys.stdin.readline

# 1676_팩토리얼 0의 개수
# N! 뒤에서 부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수..?
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1) # 재귀로 팩토리얼 하면 오버플로우

                      # 곱하면서 10으로 나눠서 나머지가 없으면 카운트,
                    # 오버플로우,
# 팩토리얼 계산후에 하면 숫자가 너무커서 메모리 넘치는듯
# 문제설명: 소인수분해의 성질을 활용하여 N!의 끝에 0이 얼마나 많이 오는지 구하는 문제
# 0이 들어가려면 (2x5) 한묶음이 하나..? 10 = 2 x 5
N = int(input())
cnt_2 = 0
cnt_5 = 0
for i in range(N+1):
    while True:
        if i == 0:          # 종료조건에 0,
            break
        elif i % 2 == 0:
            i = i / 2
            cnt_2 += 1
        elif i % 5 == 0:
            i = i / 5
            cnt_5 += 1
        else:
            break
print(min(cnt_2, cnt_5))