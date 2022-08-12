import sys
import math
sys.stdin = open('13_5.txt')
input = sys.stdin.readline
R = int(input())

print(round(float(R**2 * math.pi),5))
print(float(R**2 * 2))
