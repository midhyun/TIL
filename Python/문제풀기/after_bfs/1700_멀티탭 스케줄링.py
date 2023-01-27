import sys
sys.stdin = open('1700_멀티탭 스케줄링.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [*map(int, input().split())]
count = [0] * (k+1)
result = 0
if k <= n:
    print(0)
    exit()

for num in nums:
    count[num] += 1

now = {}
m = 0
for i in range(k):
    if len(now) == n:
        m = i        
        break
    count[nums[i]] -= 1
    now[nums[i]] = count[nums[i]]

for i in range(m, k):
    if nums[i] in now:
        count[nums[i]] -= 1
        now[nums[i]] = count[nums[i]]
        continue
    temp = min(now.values())
    if temp == 0:
        for key, v in now.items():
            if v == 0:
                del now[key]
                break
    else:
        far = -1
        val = -1
        for key in now.keys():
            idx = nums[i:].index(key)
            if far < idx:
                far = idx
                val = key
        del now[val]
    result += 1
    count[nums[i]] -= 1
    now[nums[i]] = count[nums[i]]

print(result)