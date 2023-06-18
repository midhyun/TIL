import sys
sys.stdin = open('15810_풍선공장.txt')
input = sys.stdin.readline



def Binary_Search():
    N, M = map(int, input().split())
    times = [*map(int, input().split())]

    s, e = 0, min(times)*M
    while s < e:
        mid = (s+e)//2
        tmp = 0
        for time in times:
            tmp += (mid // time)
        if tmp < M:
            s = mid + 1
        else:
            e = mid

    return s

print(Binary_Search())