import sys
from collections import defaultdict, deque
sys.stdin = open('21276_계보복원가호석.txt')
input = sys.stdin.readline

# 사람의 수
N = int(input())

# 사람들의 이름 ( 정렬 )
people = sorted(input().rstrip().split())

# 관계의 수
M = int(input())

# 진입차수, 자식리스트, 관계그래프
indegree = defaultdict(int)
info_children = defaultdict(list)
graph = defaultdict(list)

for _ in range(M):
    child, parent = input().rstrip().split()
    # 부모 -> 자식 단방향 그래프
    graph[parent].append(child)
    indegree[child] += 1

root_list = []
# 진입차수가 0인 노드는 root
for person in people:
    # people을 순회하면서 진입차수를 확인하는데 defaultdict(int)은 키가 없으면 0을 값으로 갖는 키 생성 
    if not indegree[person]:
        root_list.append(person)
root_list.sort()

# 위상정렬
q = deque(root_list)
while q:
    cur = q.popleft()
    for child in graph[cur]:
        indegree[child] -= 1
        if indegree[child] == 0:
            info_children[cur].append(child)
            q.append(child)

# 조상의 수, 이름 출력
print(len(root_list))
print(*root_list)

# person의 이름, 자식의 수, 자식 리스트 출력
for person in people:
    print(person, len(info_children[person]), *sorted(info_children[person]))