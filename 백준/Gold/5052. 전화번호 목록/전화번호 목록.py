import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        current_node = self.root
        for num in number:
            if num not in current_node.children:
                current_node.children[num] = TrieNode()
            current_node = current_node.children[num]

    def starts_with(self, prefix):
        current_node = self.root
        for num in prefix:
            if num not in current_node.children:
                return False
            current_node = current_node.children[num]
        return True



def solution():
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input().strip())
    numbers.sort(reverse=True)
    trie = Trie()
    for num in numbers:
        if trie.starts_with(num):
            return False
        trie.insert(num)
    return True

test_case = int(input())
for _ in range(test_case):
    if solution():
        print('YES')
    else:
        print('NO')
