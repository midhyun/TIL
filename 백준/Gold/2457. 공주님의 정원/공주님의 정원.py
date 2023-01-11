import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    s = a*100 + b
    e = c*100 + d
    nums.append((s, e))

nums.sort()
temp = 301
temp_list = []
cnt = 0
for s, e in nums:
    if s <= temp:
        if e >= 1201:
            cnt += 1
            temp = e
            break
        temp_list.append(e)
    elif temp_list:
        temp = max(temp_list)
        if temp < s:
            break
        temp_list = [e]
        cnt += 1
        if e >= 1201:
            cnt += 1
            temp = e
            break

if temp < 1201:
    cnt = 0
print(cnt)