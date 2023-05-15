import sys
sys.stdin = open('2887_행성터널.txt')
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
    # 더 작은 부모로 합집합 연산
    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b

result = 0
N = int(input())
locations = []
for i in range(N):
    x, y, z = map(int, input().split())
    locations.append((x, y, z, i))

dist = []
# x, y, z 좌표별 간선정보 추가
for pos in range(3):
    # 정렬 수행으로 x좌표간 최소거리 간선정보
    locations.sort(key=lambda v: v[pos])

    for i in range(1, N):
        dist.append((locations[i-1][3], locations[i][3], abs(locations[i][pos] - locations[i-1][pos])))
# 비용순으로 정렬함.
dist.sort(key=lambda v: v[2])

# 부모 테이블 상에서, 부모를 자기자신으로 초기화
parent_table = [i for i in range(N)]
# 정렬된 간선들을 하나씩 확인하며
for a, b, distance in dist:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(a) != find_parent(b):
        result += distance
        union_parent(a, b)

print(result)