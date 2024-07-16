import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    numbers = [ [int(val), i] for i, val in enumerate(input().split(), 1)]
    seg_tree = [0] * (4 * N)
    M = int(input())

    def seg_init(start, end, index):
        if start == end:
            seg_tree[index] = numbers[start]
            return seg_tree[index]
        mid = (start + end) // 2
        seg_tree[index] = min(seg_init(start, mid, index*2), seg_init(mid+1, end, index*2+1))
        return seg_tree[index]
    
    def seg_update(start, end, index, update_index, update_value):
        if update_index < start or update_index > end:
            return [sys.maxsize, 0]
        if start == end:
            seg_tree[index] = update_value
            return seg_tree[index]
        mid = (start + end) // 2
        seg_update(start, mid, index*2, update_index, update_value)
        seg_update(mid+1, end, index*2+1, update_index, update_value)

        seg_tree[index] = min(seg_tree[index*2], seg_tree[index*2+1])
    
    def find_min(start, end, index, left, right):
        if left > end or right < start:
            return [sys.maxsize, 0]
        if left <= start and end <= right:
            return seg_tree[index]
        mid = (start + end) // 2
        return min(find_min(start, mid, index*2, left, right), find_min(mid+1, end, index*2+1, left, right))
    
    seg_init(0, N-1, 1)

    for _ in range(M):
        query = list(map(int, input().split()))
        if query[0] == 1:
            numbers[query[1]-1][0] = query[2]
            seg_update(0, N-1, 1, query[1]-1, numbers[query[1]-1])
        else:
            print(find_min(0, N-1, 1, query[1]-1, query[2]-1)[1])

solution()