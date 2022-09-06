import sys
sys.stdin = open('1228_전쟁.txt')
input = sys.stdin.readline

n, w = map(int, input().split())
countries = []
for i in range(n):
    lst = input().strip().split()
    lst[1] = int(lst[1])
    lst = tuple(lst)
    countries.append(lst)
print(len(countries[1]))
