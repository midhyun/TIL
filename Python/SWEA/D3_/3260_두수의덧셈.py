import sys
sys.stdin = open('3260_두수의덧셈.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1,t+1):
    a, b = map(int, input().split())
    print(a+b)