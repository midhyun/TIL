import sys
sys.stdin = open('3003.txt')

chess = [1,1,2,2,2,8]
user_chess = list(map(int, input().split()))
result = []

for i in range(len(chess)):
    result.append(chess[i] - user_chess[i])

print(*result)