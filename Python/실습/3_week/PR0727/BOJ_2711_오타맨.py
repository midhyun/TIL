import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    a, sentence = input().split()
    num_ = int(a) - 1
    print(sentence[:num_]+sentence[num_+1:])