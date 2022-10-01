import sys
sys.stdin = open('1874_스택수열.txt')
input = sys.stdin.readline

stack = []
answer = []
cur = 1
flag = 0
n = int(input())
for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)