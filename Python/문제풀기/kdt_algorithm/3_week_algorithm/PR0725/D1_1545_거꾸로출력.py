import sys
sys.stdin = open('input.txt')

for i in range(int(input()),-1,-1): # input() 부터 0 까지 출력 공백
    print(i,end=" ")