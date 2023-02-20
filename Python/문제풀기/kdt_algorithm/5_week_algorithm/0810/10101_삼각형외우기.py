import sys
sys.stdin = open('10101.txt')
input = sys.stdin.readline
angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    angle_set = set(angle)
    if len(angle_set) == 1:
        print('Equilateral')
    elif len(angle_set) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')