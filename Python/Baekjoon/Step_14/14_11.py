import sys
sys.stdin = open('14_11.txt')
input = sys.stdin.readline

# 2004_조합 0의 개수
# n개에서 m개 고르는 경우의수에서 끝자리 0의 개수를 출력?
# 0 <= m <= n <= 20억? 을팩토리얼? 숫자 더럽게 커서 시간초과..?
# 이항계수 공식 = facto(n) 더해줌 / (facto(n-m)*facto(m)) 빼줌
# 팩토리얼이 3개니까 이전문제 3번계산해서 인수분해 2,5 개수 세줌
# 문제설명 : 위와 비슷한데 N! 대신 이항계수가 들어간 문제
# 이항계수 공식 다른게 있나
n ,m = map(int, input().split())
# 1 부터 ~ n or m 까지 2의 배수, 5의 배수 개수 세기
cnt_2 = 0
cnt_5 = 0

temp = n
while True:
    if temp == 0:
        break
    temp = temp // 2
    cnt_2 += temp
temp = n
while True:
    if temp == 0:
        break
    temp = temp // 5
    cnt_5 += temp

temp = m
while True:
    if temp == 0:
        break
    temp = temp // 2
    cnt_2 -= temp
temp = m
while True:
    if temp == 0:
        break
    temp = temp // 5
    cnt_5 -= temp
temp = n-m
while True:
    if temp == 0:
        break
    temp = temp // 2
    cnt_2 -= temp
temp = n-m
while True:
    if temp == 0:
        break
    temp = temp // 5
    cnt_5 -= temp

print(min(cnt_2, cnt_5))