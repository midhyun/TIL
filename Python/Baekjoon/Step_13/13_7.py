import sys
sys.stdin = open('13_7.txt')
input = sys.stdin.readline
T = int(input())
# 어린왕자_1004
# 경계를 최소로 지나는 경로,
# 원 : 중심 점으로부터 거리가 같은 점들의 집합.
# 출발점과 행성계간의 거리, 행성계의 반지름 비교,
# 도착점과 행성계간의 거리, 행성계의 반지름 비교,
# 거리가 반지름보다 작으면 해당 행성계 안에 있음, 크면 밖에 있음 항성계 안에 있을 경우 경계를 지나가야 하므로 카운트 +1
# 항성계가 출발지와 도착지를 모두 포함하는 범위이면 경계를 지나지 않으므로 카운트안함,
for test_case in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split()) # 출발(x1, y1) 도착(x2, y2)
    n = int(input())
    cnt = 0
    for i in range(n):
        c_x, c_y, r = map(int, input().split())
        distance_start = ((c_x - x1)**2 + (c_y - y1)**2)**(1/2)
        distance_end = ((c_x - x2)**2 + (c_y - y2)**2)**(1/2)
        if distance_start < r and distance_end > r: # 출발지만 포함 / 탈출해야 하는 항성계의 수
            cnt += 1
        elif distance_start > r and distance_end < r: # 도착지만 포함 / 진입해야 하는 항성계의 수
            cnt += 1
    print(cnt) # 진입/이탈 출력