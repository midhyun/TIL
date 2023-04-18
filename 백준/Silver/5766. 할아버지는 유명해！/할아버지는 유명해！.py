import sys
input = sys.stdin.readline

def solution():
    dic = {}
    for _ in range(N):
        nums = [*map(int, input().split())]
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
    sec_val = sorted([*dic.values()])[-2]
    result = []
    for k, v in dic.items():
        if v == sec_val:
            result.append(k)
    result.sort()

    return result

# N행의 인풋이 주어지고, M개의 정수들
while True:
    N, M = map(int, input().split())
    if not (N or M):
        break
    
    print(*solution())