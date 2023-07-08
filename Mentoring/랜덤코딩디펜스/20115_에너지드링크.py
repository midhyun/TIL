import sys
sys.stdin = open('20115_에너지드링크.txt')
input = sys.stdin.readline

# 임의의 서로 다른 두 에너지 드링크를 고른다.
# 한쪽 에너지 드링크를 다른 쪽 에너지 드링크에 모두 붓는다. 붓는 과정에서 절반을 흘린다.
# 다 붓고 남은 빈 드링크는 버린다.
# 1-3 과정을 드링크가 하나가 남을 때 까지 반복한다.

N = int(input())
nums = [*map(int, input().split())]
nums.sort()
result = nums[-1]
for i in range(N-1):
    result += nums[i]/2

print(result)