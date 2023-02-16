import sys
sys.stdin = open('1071_소트.txt')
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
num_cnt = [0]*1003
for num in nums:
    num_cnt[num] += 1
# nums에 각 숫자가 몇개있는지 확인을 위한 num_cnt
# 이후 작은 숫자부터 차례로 result에 넣는다.
# cur+1이 존재할 경우 두가지 조건 분기
# cur+2 이상의 수가 존재한다면, cur를 모두 result에 넣고,
# cur+2 이상의 수 한개를 result에 넣음 ex) 1 1 3 3 4 4 >> 1 1 4
# cur+2 이상의 수가 없다면, cur+1을 모두 result에 넣고,
# cur를 result에 모두 넣음
# cur+1 이 존재하지 않을 경우 모든 cur를 result에 넣음.
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