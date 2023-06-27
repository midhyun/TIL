import sys
sys.stdin = open('4358_생태학.txt')
input = sys.stdin.readlines

trees = input()
tree_dict = {}
for tree in trees:
    tree = tree.rstrip()
    tree_dict[tree] = tree_dict.get(tree, 0) + 1
# 파이썬의 round의 동장 방식이 특이함.
# -0.5 와 0.5 를 round 했을 경우 둘다 0이 출력 됨.
# 그러나 1.5 를 round 하면 2가 출력 됨. // 파이썬의 반올림은 반올림 하려는 수가 올림, 내림 했을 대 동일하게 차이나는 경우에는 짝수 값으로 반올림 한다.
# 즉, 정확한 2.5 를 round 하면 2가 출력되지만 부동소수점의 부정확성으로 2.500000001 을 round 한다면 보다 가까운 3으로 반올림된다.
for tree in sorted(tree_dict.keys()):
    print(tree, f'{tree_dict[tree]/len(trees)*100:.4f}')