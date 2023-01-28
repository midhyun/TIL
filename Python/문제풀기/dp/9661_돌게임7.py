import sys
sys.stdin = open('9661_돌게임7.txt')
input = sys.stdin.readline

n = int(input())

x = n%5
result = [0,1,0,1,1]
print('SK') if result[x] else print('CY')