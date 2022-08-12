import sys
sys.stdin = open('13_4.txt')
input = sys.stdin.readline

melon_per_meter = int(input())
max_h = 0
max_w = 0
max_h_idx = 0
max_w_idx = 0
fence_lst = []

for i in range(6):
    direct, meter = map(int, input().split())
    fence_lst.append((direct, meter))
    if direct == 1 or direct == 2:
        if max_w < meter:
            max_w = meter
            max_w_idx = i
    else:
        if max_h < meter:
            max_h = meter
            max_h_idx = i
idx_lst = [fence_lst[max_w_idx-1], fence_lst[(max_w_idx+1)%6], fence_lst[max_h_idx-1], fence_lst[(max_h_idx+1)%6]]

product = 1
for i in fence_lst:
    if i not in idx_lst:
        product *= i[1]
result = (max_h*max_w - product) * melon_per_meter
print(result)
