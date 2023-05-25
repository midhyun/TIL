import sys
sys.stdin = open('2467_용액.txt')
input = sys.stdin.readline

# 산성은 양수, 알칼리는 음수
# 두 용액을 혼합해서 0에 가장 가까운 용액 만들기

N = int(input())
char = [*map(int, input().split())]

s, e = 0, -1
status = 1e10
result = ()
while s - e != N:
    tmp = char[s] + char[e]
    if abs(tmp) < status:
        status = abs(tmp)
        result = (s, e)

    if tmp > 0:
        e -= 1
    elif tmp < 0:
        s += 1
    else:
        break

print(char[result[0]], char[result[1]])