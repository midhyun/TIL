import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def topological_sort(N, M, recipes, L, available):
    # 진입차수를 저장할 리스트
    indegree = [[] for _ in range(N + 1)]
    # 레시피 그래프를 생성하기 위한 딕셔너리
    graph = defaultdict(list)
    # 결과를 저장할 집합
    possible_potions = set()
    # 레시피의 수
    recipe_count = [0] * (N + 1)
    # 방문처리
    visited = [False] * (N + 1)

    # 레시피 그래프와 진입차수를 초기화
    for recipe in recipes:
        ingredients, result = recipe[1:-1], recipe[-1]
        indegree[result].append(len(ingredients))
        for ingredient in ingredients:
            graph[ingredient].append((result, recipe_count[result]))
        
        recipe_count[result] += 1

    # 위상 정렬을 위한 큐 초기화
    q = deque()
    for potion in available:
        visited[potion] = True
        q.append(potion)
    # 위상 정렬 수행
    
    while q:
        curr = q.popleft()
        possible_potions.add(curr)
        for potion, rcnt in graph[curr]:
            indegree[potion][rcnt] -= 1
            if indegree[potion][rcnt] == 0 and not visited[potion]:
                visited[potion] = True
                q.append(potion)
    return sorted(list(possible_potions))

# 입력 받기
N, M = map(int, input().split())
recipes = [list(map(int, input().split())) for _ in range(M)]
L = int(input())
available = set(map(int, input().split()))

# 가능한 물약 찾기
result = topological_sort(N, M, recipes, L, available)
print(len(result))
print(*result)