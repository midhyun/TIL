import sys
from collections import deque
sys.stdin = open('1225_암호생성기.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n = int(input())
    nums = deque([*map(int, input().split())])
    flag = True
    while flag:
        for i in range(1,6):
            num = nums.popleft() - i
            if num <= 0:
                num = 0
                nums.append(num)
                flag = False
                break
            nums.append(num)
    print(f'#{test_case}',*list(nums))
