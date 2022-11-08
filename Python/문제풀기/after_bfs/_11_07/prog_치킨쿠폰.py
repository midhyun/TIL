import sys
sys.stdin = open('prog_치킨쿠폰.txt')
input = sys.stdin.readline

chicken = int(input())
answer = 0              # 서비스 마리 수

while chicken >= 10:
    cupon = chicken % 10 # 남은 쿠폰
    chicken //= 10       # 100 -> 10 # 100마리 먹었을 때 서비스 수
    answer += chicken    # 0 - > 10
    chicken += cupon
print(answer)