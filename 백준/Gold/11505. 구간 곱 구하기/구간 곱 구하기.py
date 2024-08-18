import sys
input = sys.stdin.readline

def init_tree(start, end, index):
    if start == end:
        segment_tree[index] = numbers[start]
        return segment_tree[index]
    mid = (start + end) // 2
    segment_tree[index] = (init_tree(start, mid, index*2) * init_tree(mid+1, end, index*2+1)) % MOD
    return segment_tree[index]

def find_seg(start, end, left, right, index):
    # start, end: 현재 idx노드의 구간, segment_tree[index]: start ~ end 까지의 누적곱
    # left, right: 구하고자 하는 누적곱 구간
    # 곱해야하는 숫자가 하나도 없다면, 현재 구간에 포함되는 숫자가 하나도 없으므로 더이상 재귀하면서 곱하지않고 return 1
    if end < left or right < start:
        return 1
    # 곱해야하는 구간이 완전히 포함되어 있으므로 그대로 값을 리턴함 == 곱함
    if left <= start and end <= right:
        return segment_tree[index]
    mid = (start + end) // 2
    # 현재구간의 일부구간만을 곱해야 하므로 재귀해서 완전히 포함하는구간과 포함되지 않는 구간을 구함.
    return (find_seg(start, mid, left, right, index*2) * find_seg(mid+1, end, left, right, index*2+1)) % MOD

def update(start, end, index, update_idx, exist_value, new_value):
    if update_idx < start or end < update_idx:
        return segment_tree[index]
    if start == end:
        segment_tree[index] = new_value
        return new_value
    mid = (start + end) // 2
    segment_tree[index] = (update(start, mid, index*2, update_idx, exist_value, new_value) * update(mid+1, end, index*2+1, update_idx, exist_value, new_value)) % MOD
    return segment_tree[index]

MOD = 1000000007
N, M, K = map(int, input().split())
segment_tree = [0]*(4*N)
numbers = [int(input()) for _ in range(N)]

init_tree(0, N-1, 1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N-1, 1, b-1, numbers[b-1], c)
        numbers[b-1] = c
    else:
        print(find_seg(0, N-1, b-1, c-1, 1))