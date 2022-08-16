import sys
sys.stdin = open('1436.txt')
input = sys.stdin.readline

N = int(input())
lst = []
num = 666
while not len(lst) == N:
    if '666' in str(num):
        lst.append(num)
    num += 1

print(lst[-1])