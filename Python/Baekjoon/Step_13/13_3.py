import sys
sys.stdin = open('13_3.txt')
input = sys.stdin.readline

while True:
    tri_ = sorted(list(map(int, input().split())))
    if sum(tri_) == 0:
        break
    tri_2 = [x**2 for x in tri_]
    if tri_2[0]+ tri_2[1] == tri_2[2]:
        print('right')
    else: print('wrong')