import sys
from collections import deque
sys.stdin = open('14395_4연산.txt')
input = sys.stdin.readline

s, t = map(int, input().split())
q = deque()
check = set()
q.append((s, ''))
check.add(s)
MAX = 10e9

if s == t:
    print(0)
else:
    result = -1
    while q:
        i, path = q.popleft()
        if i == t:
            result = path
            print(result)
            exit(0)
        ni = i * i
        if 0 <= ni <= MAX and ni not in check:
            q.append((ni, path+'*'))
            check.add(ni)
        
        ni = i + i
        if 0 <= ni < MAX and ni not in check:
            q.append((ni, path+'+'))
            check.add(ni)
        
        ni = 1
        if ni not in check:
            q.append((ni, path+'/'))
            check.add(ni)
    print(result)