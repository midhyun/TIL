import sys
sys.stdin = open('14428_수열과쿼리16.txt')
input = sys.stdin.readline

def solution():
    N = int(input())
    numbers = [ [int(val), i] for i, val in enumerate(input().split(), 1)]
    seg_tree = [0] * (4 * N)
    M = int(input())

    # 트리 초기화
    def seg_init(start, end, index):
        if start == end:
            seg_tree[index] = numbers[start]
            return seg_tree[index]
        mid = (start + end) // 2
        seg_tree[index] = min(seg_init(start, mid, index*2), seg_init(mid+1, end, index*2+1))
        return seg_tree[index]
    
    # 트리 업데이트
    def seg_update(start, end, index, update_index, update_value):
        # 업데이트 인덱스가 범위를 벗어나면 최대값 리턴
        if update_index < start or update_index > end:
            return [sys.maxsize, 0]
        # 현재 인덱스가 리프노드이면 업데이트 값으로 변경
        # 범위 내에서 도달 가능한 리프노드의 인덱스는 1개이므로 update_value 갱신
        if start == end:
            seg_tree[index] = update_value
            return seg_tree[index]
        mid = (start + end) // 2
        # 재귀로 리프노드까지 내려가면서 업데이트
        seg_update(start, mid, index*2, update_index, update_value)
        seg_update(mid+1, end, index*2+1, update_index, update_value)
        # 리프노드에서 부모노드로 올라오면서 최소값 갱신
        seg_tree[index] = min(seg_tree[index*2], seg_tree[index*2+1])
    
    # 최소값 인덱스 찾기
    def find_min(start, end, index, left, right):
        # 범위를 벗어나면 최대값 리턴
        if left > end or right < start:
            return [sys.maxsize, 0]
        # 범위 내에 있으면 최소값 리턴
        if left <= start and end <= right:
            return seg_tree[index]
        mid = (start + end) // 2
        # 범위 내에 있으면 최소값 리턴
        return min(find_min(start, mid, index*2, left, right), find_min(mid+1, end, index*2+1, left, right))
    
    seg_init(0, N-1, 1)

    for _ in range(M):
        query = list(map(int, input().split()))
        if query[0] == 1:
            numbers[query[1]-1][0] = query[2]
            seg_update(0, N-1, 1, query[1]-1, numbers[query[1]-1])
        else:
            print(find_min(0, N-1, 1, query[1]-1, query[2]-1)[1])
    return    
solution()