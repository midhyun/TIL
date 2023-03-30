import sys
input = sys.stdin.readline

# 재귀 함수를 이용한 동적 계획법
def func(left, right):
    # 기저점 = 전구 자기자신
    if left == right:
        return 0
    
    # 이미 구한 dp값 존재
    if dp[left][right] != 0:
        return dp[left][right]
    
    # 기저부터 dp[][] 값을 찾아서 넣어준다.
    dp[left][right] = sys.maxsize
    for i in range(left, right):
        # 양쪽 구간의 색이 같은 경우: 0 vs 다른 경우: 1
        tmp = 1 if bulb[left] != bulb[i+1] else 0
        dp[left][right] = min(dp[left][right], func(left, i) + func(i+1, right) + tmp)
    
    return dp[left][right]


# 입력 받기
N, K = map(int, input().split())
bulb = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

# 결과 출력
print(func(0, N-1))