import sys
from collections import defaultdict
input = sys.stdin.readline

class Node():
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

def solution():
    def preOrder(Node):
        print(Node, end='')
        if tree[Node][0] != ".":
            preOrder(tree[Node][0])
        if tree[Node][1] != ".":
            preOrder(tree[Node][1])
    
    def inOrder(Node):
        if tree[Node][0] != ".":
            inOrder(tree[Node][0])
        print(Node, end='')
        if tree[Node][1] != ".":
            inOrder(tree[Node][1])
    
    def postOrder(Node):
        if tree[Node][0] != ".":
            postOrder(tree[Node][0])
        if tree[Node][1] != ".":
            postOrder(tree[Node][1])
        print(Node, end='')
    
    N = int(input())
    tree = defaultdict(list)

    for _ in range(N):
        root, left, right = input().split()
        tree[root] = [left, right]

    preOrder("A")
    print()
    inOrder("A")
    print()
    postOrder("A")
    print()
        
solution()
