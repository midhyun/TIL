import sys
from datetime import datetime
sys.stdin = open('1948_날짜계산기.txt')
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    print(int(datetime(1,m2,d2) - datetime(1,m1,d1)))