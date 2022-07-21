T = int(input())
for test_case in range(1,T+1):
    H, W, N = map(int, input().split())
    floor_num = H if N % H == 0 else N % H
    room_num = ((N-1) // H) + 1
    print(f'{floor_num}{room_num:>02}')