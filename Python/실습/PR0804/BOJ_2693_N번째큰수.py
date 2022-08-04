import sys
sys.stdin = open('2693.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[-3])