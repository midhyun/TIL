import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    result = 0
    stack = [int(input())]
    for _ in range(N-1):
        cur = int(input())
        while stack:
            if cur >= stack[-1]:
                stack.pop()
            else:
                break
        result += len(stack)
        stack.append(cur)
    
    print(result)

solution()