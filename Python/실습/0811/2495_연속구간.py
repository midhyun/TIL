import sys
sys.stdin = open('2495.txt')
input = sys.stdin.readline

for i in range(3):
    nums = list(input().strip())
    before = nums[0]
    lst = []
    cnt = 1
    for j in range(1,len(nums)):
        if nums[j] == before:
            cnt += 1
        else:
            lst.append(cnt)
            cnt = 1
            before = nums[j]
    else:
        lst.append(cnt)
    print(max(lst))

