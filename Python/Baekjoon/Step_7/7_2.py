N = int(input())
result = 1
cnt = 1
while result < N:
    result += 6*cnt
    cnt += 1
print(cnt)