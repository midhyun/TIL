import sys
sys.stdin = open('13_6.txt')
input = sys.stdin.readline
T = int(input())
for test_case in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance_ = abs(((x2-x1)**2 + (y2-y1)**2)**(1/2))
    if (x1,y1) == (x2,y2):
        if r1 == r2:
            print(-1)
        else :
            print(0)
    elif distance_ == abs(r1 - r2):
        print(1)
    elif distance_ < abs(r1 - r2):
        print(0)
    elif distance_ < r1 + r2:
        print(2)
    elif distance_ == r1 + r2:
        print(1)
    elif distance_ > r1 + r2:
        print(0)