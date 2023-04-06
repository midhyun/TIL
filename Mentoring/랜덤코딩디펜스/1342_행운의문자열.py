import sys
from itertools import permutations
sys.stdin = open('1342_행운의문자열.txt')
input = sys.stdin.readline

S = input().strip()
N = len(S)
cnt = 0

def check(word):
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            return False
    return True

for permu in set(permutations(S)):
    if check(permu):
        cnt += 1

print(cnt)