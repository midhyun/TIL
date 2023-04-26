import sys
sys.stdin = open('17128_소가정보섬.txt')
input = sys.stdin.readline
def solution():
    N, Q = map(int, input().split())
    scores = [*map(int, input().split())]
    treat_cow = [*map(int, input().split())]

    result = [scores[0] * scores[-1] * scores[-2] * scores[-3]]
    
    for i in range(1, N):
        tmp = result[-1] // scores[i-4] * scores[i]
        result.append(tmp)

    summary = sum(result)
    for treat in treat_cow:
        for i in range(treat-1, treat+3):
            idx = i % N
            result[idx] = -result[idx]
        print(result)
        print(sum(result))

solution()