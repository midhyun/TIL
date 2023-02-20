from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    lst = []
    string = list(input().strip())
    for i in string:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if '(' in lst:
                lst.pop()
            else : 
                lst.append(i)
                break
    if len(lst) == 0:
        print('YES')
    else : print('NO')