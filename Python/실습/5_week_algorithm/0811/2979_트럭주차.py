import sys
sys.stdin = open('2979.txt')
input = sys.stdin.readline

fee_table = [0, *map(int, input().split())]
parking_time = [tuple(map(int, input().split())) for _ in range(3)]
print(parking_time)
fee = 0
parking_area = []
for i in range(1, 101):
    for j in range(3):
        if parking_time[j][0] == i:
            parking_area.append(j)
        if parking_time[j][1] == i:
            parking_area.pop()
    fee += fee_table[len(parking_area)]*len(parking_area)
print(fee)