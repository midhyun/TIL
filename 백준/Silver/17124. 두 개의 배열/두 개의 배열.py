import sys
input = sys.stdin.readline

def findMin(d):
  now = d[2]
  rst = 2
  if d[1] <= now:
    now = d[1]
    rst = 1
  if d[0] <= now:
    now = d[0]
    rst = 0
  return rst
 
def binary(cur, B, start, end):
  diff = end - start
  if diff <= 1:
    return start
  mid = (start + end) // 2
  if cur < B[mid]:
    return binary(cur, B, start, mid)
  else: # cur >= B[mid]
    return binary(cur, B, mid, end)
 
def solve():
  n, m = [int(x) for x in input().split()]
  A = [int(x) for x in input().split()]
  B = [int(x) for x in input().split()]
  B.sort()
  s = 0
  for cur in A:
    p = binary(cur, B, 0, m)
    d = []
    d.append(abs(B[p-1] - cur))
    d.append(abs(B[p] - cur))
    d.append(abs(B[(p+1)%m] - cur))
    idx = findMin(d)
    s += B[p + idx - 1]
  print(s)

t = int(input())
for _ in range(t):
  solve()