import sys
sys.stdin = open('2628_종이자르기.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
cut = int(input())
col = [0,m]
row = [0,n]
for _ in range(cut):
    vector, line_ = map(int, input().split())
    if vector == 1:
        col.append(line_)
    else:
        row.append(line_)
col = sorted(col,reverse=True)
row = sorted(row,reverse=True)

col_m = 0
row_m = 0
for i in range(1,len(col)):
    if col[i-1]-col[i] > col_m:
        col_m = col[i-1]-col[i]
for i in range(1,len(row)):
    if row[i-1]-row[i] > row_m:
        row_m = row[i-1]-row[i]
print(col_m*row_m)