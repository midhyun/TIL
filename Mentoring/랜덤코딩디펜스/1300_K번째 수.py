import sys
sys.stdin = open('1300_K번째 수.txt')
input = sys.stdin.readline

N = int(input())
K = int(input())

def binarySearch(target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid//i, N)

        if cnt >= target:
            end = mid - 1
        else:
            start = mid + 1
        
    return start

print(binarySearch(K,1,N*N))
# 전체 숫자들 중에서 mid보다 작거나 같은 숫자의 개수가 K보다 작아질 때 정답.