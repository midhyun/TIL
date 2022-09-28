import sys
sys.stdin = open('1244_최대상금.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    board, cnt = map(int, input().split())
    board = list(str(board))
    print(board)