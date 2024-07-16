import sys
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    segment_tree = [0] * (4*N)
    numbers = [int(input()) for _ in range(N)]

    def tree_init(start, end, index):
        if start == end:
            segment_tree[index] = numbers[start]
            return segment_tree[index]
        mid = (start + end) // 2
        segment_tree[index] = tree_init(start, mid, index*2) + tree_init(mid+1, end, index*2+1)
        return segment_tree[index]
    
    def find(start, end, left, right, index):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return segment_tree[index]
        mid = (start + end) // 2
        return find(start, mid, left, right, index*2) + find(mid+1, end, left, right, index*2+1)
    
    def update(start, end, index, update_idx, new_value):
        if update_idx < start or update_idx > end:
            return
        segment_tree[index] += new_value
        if start == end:
            return
        mid = (start + end) // 2
        update(start, mid, index*2, update_idx, new_value)
        update(mid+1, end, index*2+1, update_idx, new_value)
    
    tree_init(0, N-1, 1)
    for _ in range(M+K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(0, N-1, 1, b-1, c-numbers[b-1])
            numbers[b-1] = c
        else:
            print(find(0, N-1, b-1, c-1, 1))

solution()