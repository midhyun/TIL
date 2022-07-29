import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    square = list(map(int, input().split()))
    if square.count(square[0]) == 1:
        print(f'#{test_case} {square[0]}')
    elif square.count(square[1]) == 1:
        print(f'#{test_case} {square[1]}')
    else: print(f'#{test_case} {square[2]}')
