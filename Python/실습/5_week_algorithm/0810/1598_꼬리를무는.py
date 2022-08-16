import sys
sys.stdin = open('1598.txt')
input = sys.stdin.readline

num_1, num_2 = map(int, input().split())

len_row = abs(((num_2 - 1) // 4) - ((num_1 - 1) // 4))
col_idx = [4,1,2,3]
len_col = abs((col_idx[num_2 % 4]) - (col_idx[num_1 % 4]))

print(len_row + len_col)