import sys
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
