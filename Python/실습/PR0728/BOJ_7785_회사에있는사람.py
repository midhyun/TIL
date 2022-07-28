import sys
sys.stdin = open('input.txt')

n = int(input())
giggle_dict = {}
lst = []
for i in range(n):
    A, B = map(str,input().split())
    giggle_dict[A] = B

for i in giggle_dict:
    if giggle_dict[i] == 'enter':
        lst.append(i)

lst.sort(reverse = True )
for i in lst:
    print(i)