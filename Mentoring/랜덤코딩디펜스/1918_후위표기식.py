import sys
sys.stdin = open('1918_후위표기식.txt')
input = sys.stdin.readline

def sol(enter):
    stack = []

    for i in range(len(enter)):
        if enter[i] == '(':
            stack.append(enter[i])
        elif enter[i] == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        elif enter[i] == '+' or enter[i] == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(enter[i])
        elif enter[i] == '*' or enter[i] == '/':
            while stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(enter[i])  
        elif "A" <= enter[i] <= 'Z':
            print(enter[i], end='')

    while stack:
        print(stack.pop(), end='')

sol(input().rstrip())
print()