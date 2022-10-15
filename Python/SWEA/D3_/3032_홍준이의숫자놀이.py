import sys
from math import gcd
sys.stdin= open('3032_홍준이의숫자놀이.txt')
input = sys.stdin.readline
a, b = map(int, input().split())

gcd(a, b)
