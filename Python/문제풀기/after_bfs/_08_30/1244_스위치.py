import sys
sys.stdin = open('1244_스위치.txt')
input = sys.stdin.readline

n_swi = int(input())
switch_ = [*map(int, input().split())]
n_stu = int(input())

for _ in range(n_stu):
    s, n = map(int, input().split())
    n = n-1
    if s == 1:
        for i in range(n, n_swi, n+1):
            switch_[i] = not switch_[i]
    else:
        a = 1
        while 1:
            left_ = n-a
            right_ = n+a
            if 0 <= left_ < n and 0 <= right_ < n_swi and switch_[left_] == switch_[right_]:
                a += 1
            else:
                for i in range(left_+1, right_):
                        switch_[i] = not switch_[i]
                break

cnt = 0
while cnt < n_swi:
    print(switch_[cnt]*1, end= ' ')
    if cnt % 20 == 19:
        print()
    cnt += 1