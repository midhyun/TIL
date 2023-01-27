import sys
sys.stdin = open('9659_돌게임5.txt')
input = sys.stdin.readline

n = int(input())
answer = [0,1,0,1,1,1,1]
print('SK') if answer[n%7] else print('CY')