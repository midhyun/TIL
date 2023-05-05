import sys
import math
sys.stdin = open('1935_후위표기식2.txt')
input = sys.stdin.readline

N = int(input())
words = list(input().rstrip())
nums = [0]*N
for i in range(N):
    nums[i] = int(input())

stack = []

for word in words:
    if 'A' <= word <= 'Z':
        stack.append(nums[ord(word)-65])
    
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if word == '*':
            stack.append(num1*num2)
        elif word == '+':
            stack.append(num1+num2)
        elif word == '-':
            stack.append(num1-num2)
        elif word == '/':
            stack.append(num1/num2)

print(f'{stack[0]:.2f}')
