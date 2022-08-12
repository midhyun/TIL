import sys
sys.stdin = open('13_2.txt')
input = sys.stdin.readline
lst_x = {}
lst_y = {}
for _ in range(3):
    x, y = map(int, input().split())
    lst_x[x] = lst_x.get(x, 0) + 1
    lst_y[y] = lst_y.get(y, 0) + 1
result_x =[k for k, v in lst_x.items() if v == min(lst_x.values())]
result_y =[k for k, v in lst_y.items() if v == min(lst_y.values())]
print(*result_x, *result_y)