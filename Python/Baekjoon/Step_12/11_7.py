import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('11_7.txt')
input = sys.stdin.readline
s = input().strip()
n = len(s)
lst = []
x = 1
def facto(num, a):
    if num == 0:
        return
    for i in range(a):
        lst.append(s[i:i+num])

    facto(num-1, a+1)

facto(n, x)
print(len(set(lst)))