import sys
input = sys.stdin.readline

n = int(input())

x = n%5
result = [0,1,0,1,1]
print('SK') if result[x] else print('CY')