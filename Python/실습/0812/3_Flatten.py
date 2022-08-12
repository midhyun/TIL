import sys

sys.stdin = open("_Flatten.txt")
T= 10

for test_case in range(1, T+1):
    dump = int(input())
    box_wall = list(map(int, input().split()))
    for i in range(dump):
        max_h = max(box_wall)
        max_h_idx = box_wall.index(max_h)
        min_h = min(box_wall)
        min_h_idx = box_wall.index(min_h)

        box_wall[max_h_idx] -= 1
        box_wall[min_h_idx] += 1
    
    print(f'#{test_case}', max(box_wall)-min(box_wall))
