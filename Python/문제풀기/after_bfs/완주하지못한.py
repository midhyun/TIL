from functools import partial
import sys 
sys.stdin = open('완주하지못한.txt')
input = sys.stdin.readline
participant = input().strip().split()
completion = input().strip().split()

dic_p = {}
dic_c = {}
answer = ''
for person in completion:                      # 참가자, 동명이인 명수
    dic_c[person] = dic_c.get(person, 0) + 1    # {vinco:1} 


for person in participant:
    temp = dic_c.pop(person, 0)           # True 이면?

    if temp:
        dic_c[person] = dic_c.get(person, temp-1)
    elif temp == 0:

        answer = person

print(answer)