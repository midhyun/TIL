import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('5639_이진검색트리.txt')

class Node:
    def __init__(self, root):
        self.root = root
        self.left = 0
        self.right = 0

def back_loop(now):
    if tree[now].left:
        back_loop(tree[now].left)
    if tree[now].right:
        back_loop(tree[now].right)
    print(now)
    
lines = sys.stdin.readlines()
nums = []
for line in lines:
    nums.append(int(line))
# 50 30 24 5 28 45 98 52 60

tree = {}
stack = [] # 부모 후보.

# 트리 만들기
for now in nums:
    if stack:
        if stack[-1] > now: # 현재노드는 스택의 마지막(부모)의 왼쪽노드임.
            tree[stack[-1]].left = now

        else:
            while True: # 현재 노드가 스택의 마지막값보다 큼, 부모 찾기.
                last = stack.pop()
                if not stack or stack[-1] > now: # stack[-1]보다 왼쪽, last의 오른쪽
                    tree[last].right = now
                    break

    tree[now] = Node(now)
    stack.append(now)

back_loop(nums[0])