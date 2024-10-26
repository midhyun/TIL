import sys
sys.stdin = open('14426_접두사찾기.txt')
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.isEnd = True
    
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
    
def solution():
    N, M = map(int, input().split())
    trie = Trie()

    for _ in range(N):
        word = input().strip()
        trie.insert(word)
    
    cnt = 0
    for _ in range(M):
        query = input().strip()
        if trie.starts_with(query):
            cnt += 1
    
    print(cnt)
    return

solution()
