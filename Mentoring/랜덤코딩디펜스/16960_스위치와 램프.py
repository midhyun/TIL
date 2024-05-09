import sys
sys.stdin = open('16960_스위치와 램프.txt')
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    lamp = [0]*(M+1) # 램프 별 연결된 스위치의 수
    switches = [] # 스위치 별 연결된 스위치 번호

    # lamp, switches 값 입력
    for _ in range(N):
        nums = list(map(int, input().split()))[1:]
        switches.append(nums)
        for num in nums:
            lamp[num] += 1
    # 스위치를 꺼도 꺼지는 램프가 없다면 return 1
    # 모든 스위치를 확인하는 동안 램프가 전부 켜지는 경우가 없다면 return 0
    for switch in switches:
        check = True
        for num in switch:
            if (lamp[num] - 1) == 0:
                check = False
        
        if check:
            return 1
    return 0

print(solution())