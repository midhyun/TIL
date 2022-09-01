import sys
sys.stdin = open('16139_상호작용.txt')
input = sys.stdin.readline

strs = list(input())
q = int(input())
nums = [[0]*(len(strs)) for _ in range(26)]
nums[ord(strs[0])-97][1] = 1
for i in range(2, len(strs)):
    nums[ord(strs[i-1])-97][i] = 1
    for j in range(26):
        nums[j][i] += nums[j][i-1]

for i in range(q):
    a = input().strip().split()
    result = nums[ord(a[0])-97][int(a[2])+1] - nums[ord(a[0])-97][int(a[1])]
    print(result)