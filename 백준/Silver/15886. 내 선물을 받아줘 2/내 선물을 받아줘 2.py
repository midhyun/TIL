import sys
input = sys.stdin.readline

N = int(input())
graph = list(input().rstrip())
        
result = 0
for i in range(1, N):
    if graph[i] == 'W' and graph[i-1] == 'E':
        result += 1
    
print(result)