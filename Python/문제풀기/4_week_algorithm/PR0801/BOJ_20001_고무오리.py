from collections import deque
import sys
stack = []

while True:
    order = input()
    if order == '문제':
        stack.append('문제')
    elif order == '고무오리':
        if len(stack) == 0:
            stack.append('문제')
            stack.append('문제')
        else:
            stack.pop()
    elif order =='고무오리 디버깅 끝':
        break
if len(stack) == 0:
    print('고무오리야 사랑해')
else :
    print('힝구')