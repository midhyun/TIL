import sys
sys.stdin = open('14_2.txt')
input = sys.stdin.readline
# A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니여야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램 작성,

N = int(input()) # 1 <= N <= 50

lst = sorted(list(map(int, input().split())))
print(lst[0]*lst[-1])