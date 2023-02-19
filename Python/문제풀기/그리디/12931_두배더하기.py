import sys
sys.stdin = open('12931_두배더하기.txt')
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
cnt = 0
while sum(nums):
    # 홀수가 있을 경우 1을 더했을 경우만 가능하므로 한개를 빼면서
    # 횟수를 추가해줌.
    for i in range(N):
        if nums[i] % 2 == 1:
            nums[i] -= 1
            cnt += 1
    # 빼기만으로 0을 만들 수 있는 경우 반복문 종료
    if not sum(nums):
        break
    # 홀수인 경우를 모두 빼주어서 짝수만 남았으므로 2로 나누면서
    # 횟수를 추가해줌.
    for i in range(N):
        nums[i] //= 2
    cnt += 1
# 결과 출력
print(cnt)