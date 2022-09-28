import sys
sys.stdin = open('1234_비밀번호.txt')
input = sys.stdin.readline

for test_case in range(1, 11):
    n, nums = input().strip().split()
    stack = [nums[0]]
    for num in nums[1:]:
        if len(stack) != 0 and num == stack[-1]:
            stack.pop()
        else:
            stack.append(num)
    print(f'#{test_case}',''.join(stack))