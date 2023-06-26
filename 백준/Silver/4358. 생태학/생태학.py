import sys
input = sys.stdin.readlines

trees = input()
tree_dict = {}
for tree in trees:
    tree = tree.rstrip()
    tree_dict[tree] = tree_dict.get(tree, 0) + 1

for tree in sorted(tree_dict.keys()):
    print(tree, f'{tree_dict[tree]/len(trees)*100:.4f}')