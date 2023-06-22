import sys
import re
sys.stdin = open('2671_잠수함식별.txt')
input = sys.stdin.readline
# (100~1~|01)~
sound = input().rstrip()
# ((100+1+)|(01))+

if re.fullmatch('(100+1+|01)+', sound):
    print('SUBMARINE')
else:
    print('NOISE')