import sys
sys.stdin = open('1918_후위표기식.txt')
input = sys.stdin.readline
def postfix(post):
    stack = list()

    for i in range(len(post)):
        if (post[i] == "("):
            stack.append(post[i])
        elif (post[i] == "+" or post[i] == "-"):
            while(stack and stack[-1]!='('):
                print(stack.pop(), end="")
            stack.append(post[i])
        elif (post[i] == "*" or post[i] == "/"):
            while (stack and stack[-1] != '(' and (stack[-1] == "*" or stack[-1] =='/')):
                print(stack.pop(), end="")
            stack.append(post[i])
        elif (post[i] == ")"):
            while (stack and stack[-1] != '('):
                print(stack.pop(), end="")
            stack.pop()
        elif (post[i] >= 'A' and post[i] <= 'Z'):
            print(post[i], end="")

    if (len(stack) >0):
        for i in range(len(stack)):
            print(stack.pop(), end="")


post = input().rstrip()
postfix(post)