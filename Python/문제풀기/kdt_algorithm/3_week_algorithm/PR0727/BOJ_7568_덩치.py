import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for case in range(N):
    tall, weight = map(int, input().split())
    lst.append(tall)
    lst.append(weight)
tall = lst[::2]
weight = lst[1::2]
for i in range(len(tall)):
    cnt = 1
    for j in range(len(tall)):
        if tall[i] < tall[j]:
            if weight[i] < weight[j]:
                cnt += 1
    print(cnt, end=' ')
    