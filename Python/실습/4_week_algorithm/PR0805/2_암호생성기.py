import sys
from collections import deque
sys.stdin = open("_암호생성기.txt")
input = sys.stdin.readline


for _ in range(10):                                 # 10회 반복
    test_case = int(input())
    nums = deque(list(map(int, input().split())))   # 큐에 숫자들을 담아줌
    while True:                                     # break가 나올 때 까지 순회
        if nums[-1] == 0:                           # 큐의 마지막 값이 0 이면 break
            break
        for i in range(1, 6):                       # 1사이클은 5번 반복
            if nums[0] - i <= 0:                    # num[0] - i 가 0이하 일 경우 num[0] = 0
                nums[0] = 0                         # num[0] 가 0 이면 왼쪽에서 꺼내서 맨뒤로 보내고 break
                nums.append(nums.popleft())
                break
            else:
                nums[0] = nums[0] - i               # i += 1 만큼 num[0]에서 빼주고, 0이 아니면
                nums.append(nums.popleft())         # num[0]를 왼쪽에서 꺼내서 맨뒤로 보냄
    print(f'#{test_case}',end=' ')
    print(*nums)