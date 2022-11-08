import sys
sys.stdin = open('9935_문자열폭발.txt')
input = sys.stdin.readline

string = list(input().strip())
bomb = list(input().strip())

n = len(bomb)
stack = []
for strin in string:
    stack += strin
    if strin == bomb[-1] and stack[-n:] == bomb:
        del stack[-n:]
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))