import sys
from collections import deque
sys.stdin = open('4949.txt')
input = sys.stdin.readline
run = True
while run:                              # run = True 인동안 반복
    line = input()
    lst = []
    if line == '.\n':                   # sys.stdin.readline 으로 입력을 받으면 \n 개행까지 입력을받음, .strip으로 날리면 ' .' == '.'이 되버림
        break                           # 따라서 '.\n'에서 break // 
    for i in line:                      # 문자열 하나씩 검사
        if i == '(':                    # 괄호가 열리면 스택에 쌓는다.
            lst.append(i)
        elif i == '[':                  # 닫는 괄호면 쌓여있는 스택에 여는 괄호와 모양이 같으면 continue 여는괄호가 없거나 다르면 'no', break
            lst.append(i)
        elif i == ')':
            if len(lst) == 0:
                print('no')
                break
            elif lst.pop() == '(':
                continue
            else:
                print('no')
                break
        elif i == ']':
            if len(lst) == 0:
                print('no')
                break
            elif lst.pop() == '[':
                continue
            else:
                print('no')
                break
    else:
        if len(lst) != 0:               # 위의 조건을 모두 통과하고, 스택에 값이 없을때 'yes'
            print('no')                 # 괄호가 열린채 남아있다면 == 스택에 값이 있다면, 'no'
        else: print('yes')