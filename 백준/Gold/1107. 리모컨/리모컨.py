import sys
input = sys.stdin.readline

cur = 100
channel = int(input())
L = len(str(channel))
break_btn = int(input())
btn = {i for i in range(0, 10)}
btn -= set(map(int, input().split())) if break_btn else set()
result = abs(cur - channel)

def find(num):
    global result

    if len(num) > L:
        return

    for bt in btn:
        tmp = num + str(bt)
        result = min(result, abs(channel - int(tmp)) + len(tmp))

        find(tmp)

find('') if break_btn < 10 else ''
print(result)