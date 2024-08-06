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
        print(Node.root, end='')
        if Node.left != ".":
            preOrder(tree[Node.left])
        if Node.right != ".":
            preOrder(tree[Node.right])
    
    def inOrder(Node):
        if Node.left != ".":
            inOrder(tree[Node.left])
        print(Node.root, end='')
        if Node.right != ".":
            inOrder(tree[Node.right])
    
    def postOrder(Node):
        if Node.left != ".":
            postOrder(tree[Node.left])
        if Node.right != ".":
            postOrder(tree[Node.right])
        print(Node.root, end='')

    N = int(input())
    tree = {}
    for _ in range(N):
        root, left, right = input().split()
        tree[root] = Node(root, left, right)
    
    preOrder(tree["A"])
    print()
    inOrder(tree["A"])
    print()
    postOrder(tree["A"])
    print()
        
solution()
