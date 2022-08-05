# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

C = input()
lst = list(C)
lst_rev = lst.reverse()
rev_num = ''.join(lst)
A, B = map(int, rev_num.split())
if A > B :
    print(A)
else : print(B)
