import sys
input = sys.stdin.readline
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