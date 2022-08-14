import sys
sys.stdin = open('13_8.txt')
input = sys.stdin.readline

# 하키_1358
# 디지털 카메라가 링크의 사진을 매 1 초마다 찍는다.
# 디지털 카메라가 찍은 사진에서 각 선수의 위치를 뽑아낸다.
# 하키 '링크 안에 같은 팀선수가 총 몇명'인지 계산한다.
# 링크는 W,H 직사각형 양옆에 반지름 2/H 인 반원
W, H, X, Y, P = map(int, input().split()) # P 선수의 수
cnt = 0 # 링크안에 있는 사람의 수
for _ in range(P):
    pos_x, pos_y = map(int, input().split())
    distance_L = ((X - pos_x)**2 + (Y+(H/2) - pos_y)**2)**(1/2) # 피타고라스, 왼쪽 원
    distance_R = ((X+W -pos_x)**2 + (Y+(H/2) - pos_y)**2)**(1/2) # 오른쪽 원
    if distance_L <= H/2 or distance_R <= H/2:
        cnt += 1
    elif X <= pos_x <= X+W and Y <= pos_y <= Y+H:
        cnt += 1 
print(cnt)