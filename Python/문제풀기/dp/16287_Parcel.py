import sys
sys.stdin = open('16287_Parcel.txt')
input = sys.stdin.readline

W, N = map(int, input().split())
weights = [*map(int, input().split())]
dp = [False]*(W+1)

def solution():
    # 물건들을 순회 (두번째 for문의 순서에 주의)
    for i in range(1, N):
        # i번째물건과 i이후의 물건 하나를 더한 값을 가지고
        # dp에서 w-더한값의 경우가 있다면 'YES' w를 만들 수 있음.
        for j in range(i+1, N):
            if weights[i] + weights[j] < W and dp[W-weights[i]-weights[j]]:
                return 'YES'
        # i번째 물건과 i이전의 물건 하나를 더한 값이 W보다 작으면
        # dp그래프에 True로서 삽입.
        for j in range(i):
            if weights[i] + weights[j] < W:
                dp[weights[i]+weights[j]] = True
    else:
        # W를 만들 수 있는 경우가 없이 반복문이 끝났으므로 'NO'
        return 'NO'

print(solution())