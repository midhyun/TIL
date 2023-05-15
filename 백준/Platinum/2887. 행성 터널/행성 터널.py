import sys
input = sys.stdin.readline
# 특정 원소가 속한 집합 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table[x])
    return parent_table[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    parent_table[b] = a


result = 0
N = int(input())
locations = []
for i in range(N):
    x, y, z = map(int, input().split())
    locations.append((x, y, z, i))

dist = []
for pos in range(3):
    locations.sort(key=lambda v: v[pos])
    for i in range(1, N):
        dist.append((locations[i-1][3], locations[i][3], abs(locations[i][pos] - locations[i-1][pos])))
dist.sort(key=lambda v: v[2])
#부모 테이블 상에서, 부모를 자기자신으로 초기화
parent_table = [i for i in range(N)]

for a, b, distance in dist:
    if find_parent(a) != find_parent(b):
        result += distance
        union_parent(a, b)

print(result)