import sys
sys.stdin = open('1221_GNS.txt')
input = sys.stdin.readline

nums_1 = {
    "ZRO":0,
    "ONE":1,
    "TWO":2,
    "THR":3,
    "FOR":4,
    "FIV":5,
    "SIX":6,
    "SVN":7,
    "EGT":8,
    "NIN":9
    }
nums_2 = {
    0:"ZRO",
    1:"ONE",
    2:"TWO",
    3:"THR",
    4:"FOR",
    5:"FIV",
    6:"SIX",
    7:"SVN",
    8:"EGT",
    9:"NIN"
    }
t = int(input())
for test_case in range(1, t+1):
    print('------------------',test_case)
    tc, word = input().strip().split()
    word = int(word)
    num_lst = input().strip().split()
    for i in range(word):
        num_lst[i] = nums_1[num_lst[i]]
    num_lst.sort()
    for i in range(word):
        num_lst[i] = nums_2[num_lst[i]]
    
    print(tc)
    print(*num_lst)
