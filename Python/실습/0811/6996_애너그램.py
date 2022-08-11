import sys
sys.stdin = open('6996.txt')
input = sys.stdin.readline



T = int(input())
for test_case in range(1, T+1):
    dict_a = {}
    dict_b = {}
    a, b = input().strip().split()
    for word in a:
        dict_a[word] = dict_a.get(word, 0) + 1
    for word in b:
        dict_b[word] = dict_b.get(word, 0) + 1
    if dict_a == dict_b:
        print(f'{a} & {b} are anagrams')
    else: print(f'{a} & {b} are NOT anagrams')