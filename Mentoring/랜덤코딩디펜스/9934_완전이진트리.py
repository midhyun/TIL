import sys
sys.stdin = open('9934_완전이진트리.txt')
input = sys.stdin.readline

def solution():
    K = int(input())
    arr = [*map(int, input().split())]
    tree = [0 for _ in range(2 ** K)]
    arr.reverse()

    def make_tree(tree: list, arr: list, node: int):
        # root의 idx = 1 이므로 그보다 작거나, 최대 idx를 넘어가면 재귀 종료
        if node < 1 or 2 ** K <= node: return
        # 이진트리를 리스트로 표현하면 자식노드는 root * 2, root * 2 + 1 이므로,
        # 전위순회에 따라서 왼 - 루트 - 오 순서로 트리를 리스트에 담는다.
        make_tree(tree, arr, 2 * node) # 왼쪽 자식노드로 재귀
        tree[node] = arr.pop() #
        make_tree(tree, arr, 2 * node + 1) # 오른쪽 자식노드로 재귀
    
    make_tree(tree, arr, 1)
    i = 1
    while i < 2 ** K:
        print(*tree[i:i*2])
        i*=2

    return

solution()
