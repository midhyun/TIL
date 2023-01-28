import sys
sys.stdin = open('9661_돌게임7.txt')
input = sys.stdin.readline

n = int(input())
x = n%4
if x == 2:
    print('CY')
else:
    print('SK')