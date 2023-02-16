import sys
sys.stdin = open('1071_소트.txt')
input = sys.stdin.readline

N = int(input())
nums = sorted([*map(int, input().split())])
num_cnt = [0]*1003
for num in nums:
    num_cnt[num] += 1

cur = 0; result = []
while not len(result) == N:
    if num_cnt[cur]:
        if num_cnt[cur+1]:
            for nxt in range(cur+2, 1003):
                if num_cnt[nxt]:
                    result.extend(num_cnt[cur]*[cur])
                    result.append(nxt)
                    num_cnt[cur] = 0
                    num_cnt[nxt] -= 1
                    break
            else:
                result.extend(num_cnt[cur+1]*[cur+1])
                result.extend(num_cnt[cur]*[cur])
                num_cnt[cur], num_cnt[cur+1] = 0, 0
        else:
            result.extend(num_cnt[cur]*[cur])
            num_cnt[cur] = 0
    cur += 1

print(*result)