import sys
sys.stdin = open('11723_집합.txt')
input = sys.stdin.readline

S = set()
M = int(input())
for i in range(M):
    order = input().strip()
    try:
        cal, x = order.split()
    except:
        cal = order
    if cal == 'add':
        S.add(x)
    if cal == 'remove' and x in S:
        S.remove(x)
    if cal == 'check':
        print(1) if x in S else print(0)        
    if cal == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    if cal == 'all':
        S = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    if cal == 'empty':
        S = set()
# 비트 마스킹 풀이
for _ in range(M):
    o = sys.stdin.readline().split()
    if o[0] == "add":
        S |= (1 << int(o[1]))
    elif o[0] == "remove":
        S &= ~(1 << int(o[1]))
    elif o[0] ==  "check":
        print(1 if S & (1 << int(o[1])) else 0)
    elif o[0] == "toggle":
        S ^= (1 << int(o[1]))
    elif o[0] == "all":
        S = (2 ** 21) - 1
    else:
        S = 0