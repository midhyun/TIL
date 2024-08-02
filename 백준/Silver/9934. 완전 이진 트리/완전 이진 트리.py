import sys
input = sys.stdin.readline

def solution():
    K = int(input())
    arr = [*map(int, input().split())]
    tree = [0 for _ in range(2 ** K)]

    def make_tree(tree: list, arr: list, node: int):
        if node < 1 or 2 ** K <= node: return
        make_tree(tree, arr, 2 * node + 1) 
        tree[node] = arr.pop()
        make_tree(tree, arr, 2 * node) 
        
    make_tree(tree, arr, 1)
    i = 1
    while i < 2 ** K:
        print(*tree[i:i*2])
        i*=2

    return

solution()
