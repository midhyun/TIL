import sys
import re
input = sys.stdin.readline
# (100~1~|01)~
sound = input().rstrip()
# (100+1+)|(01)+

if re.fullmatch('(100+1+|01)+', sound):
    print('SUBMARINE')
else:
    print('NOISE')