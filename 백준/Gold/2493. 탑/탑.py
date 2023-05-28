import sys
input = sys.stdin.readline

N = int(input())
heights = [*map(int, input().split())]
stack = [N-1]
result = [0]*N
for i in range(N-2, -1, -1):
    
    while stack:
        if heights[stack[-1]] < heights[i]:
            result[stack.pop()] = i + 1
        else:
            break
    if not stack or heights[stack[-1]] > heights[i]:
        stack.append(i)

print(*result)
