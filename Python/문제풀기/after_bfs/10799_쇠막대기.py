import sys
sys.stdin = open('10799_쇠막대기.txt')
input = sys.stdin.readline


array = list(input().strip())


result = 0
cnt = 0
stack = []
for arr in array:
    if arr == '(':
        stack.append(arr)
        cnt += 1
    elif arr == ')':
        check = stack.pop()
        if check == '(':
            stack.append(')')
            cnt -= 1
            result += cnt
        else:
            stack.append(')')
            cnt -= 1
            result += 1
print(stack)
print(result)