import sys
sys.stdin = open('9610.txt')
input = sys.stdin.readline

n = int(input())
lst = [0]*5
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:                # x or y 가 0일 경우 좌표가 평행선 위에 있으므로 AXIS += 1
        lst[4] += 1
    elif x > 0:                         # 각 사분면에 해당하는 좌표이므로 값 증가.
        if y > 0:
            lst[0] += 1
        else:
            lst[3] += 1
    else:
        if y > 0:
            lst[1] += 1
        else:
            lst[2] += 1
for i in range(4):
    print(f'Q{i+1}: {lst[i]}')
print(f'AXIS: {lst[4]}')