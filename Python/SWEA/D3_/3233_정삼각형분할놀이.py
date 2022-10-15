import sys
sys.stdin = open('3233_정삼각형분할놀이.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    a, b = map(int, input().split())
    print(f'#{test_case}', int((a*a)/(b*b)))