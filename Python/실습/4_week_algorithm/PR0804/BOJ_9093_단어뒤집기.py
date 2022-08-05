import sys
sys.stdin = open('9093.txt')
input = sys.stdin.readline

T = int(input())

for i in range(T):
    lst_word = input().split()
    for j in lst_word:
        print(j[::-1],end =' ')
    print()