import sys
sys.stdin = open('2887_행성터널.txt')
input = sys.stdin.readline

def find_parent(cur):
    if parent_table[cur] == cur:
        return cur
    else:
        parent_table[cur] = find_parent(parent_table[cur])
        return parent_table[cur]

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
    before_location = locations[0][3]
    for i in range(1, N):
        cur_location = locations[i][3]
        dist.append((before_location, cur_location, abs(locations[i][pos] - locations[i-1][pos])))
dist.sort(key=lambda v: v[2])

parent_table = [i for i in range(N)]
for a, b, distance in dist:
    if find_parent(a) != find_parent(b):
        result += distance
        union_parent(a, b)

print(result)