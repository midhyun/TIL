import sys
sys.stdin = open('2864.txt')
input = sys.stdin.readline

A, B = map(str, input().split())

# 최대 = 5를 6으로
print(int(A.replace('6', '5'))+int(B.replace('6', '5')),end = ' ')
# 최소 = 6을 5로
print(int(A.replace('5', '6'))+int(B.replace('5', '6')))