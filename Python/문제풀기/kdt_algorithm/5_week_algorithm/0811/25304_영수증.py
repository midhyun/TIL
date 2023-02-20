import sys
sys.stdin = open('25304.txt')
input = sys.stdin.readline

X = int(input())    # 총 금액
N = int(input())    # 물건 종류의 수
lst = [tuple(map(int, input().split())) for _ in range(N)]
sum_ = sum([ x[0]* x[1] for x in lst])
if X == sum_:
    print('Yes')
else:
    print('No')
