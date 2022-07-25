# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

mul =str(A*B*C)
lst = [0]*10
for cnt in mul:
    lst[int(cnt)] += 1
    
for prt in lst:
    print(prt)
