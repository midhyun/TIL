# https://school.programmers.co.kr/learn/courses/15008/lessons/121685

import sys
sys.stdin = open('pccp_유전법칙.txt')
input = sys.stdin.readline
n = int(input())
rr = [1,1,1,1]
rx = [1,2,2,3]
xx = [3,3,3,3]
queries = []
for i in range(n):
    queries.append([*map(int, input().split())])
answer = []
for query in queries:
    g, n = query
    n -= 1
    dna = []
    for i in range(g-1):
        dna.append(n%4)
        n = n//4
    bean = 2
    for i in range(g-1):
        x = dna.pop()
        if bean == 1:
            bean = rr[x]
        elif bean == 2:
            bean = rx[x]
        elif bean == 3:
            bean = xx[x]
    if bean == 1:
        answer.append("RR")
    elif bean == 2:
        answer.append("Rr")
    elif bean == 3:
        answer.append("rr")

print(answer)