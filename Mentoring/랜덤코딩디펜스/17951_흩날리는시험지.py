import sys
sys.stdin = open('17951_흩날리는시험지.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
scores = [*map(int, input().split())]

def binary_Search():
    min_score = 0
    max_score = 20*N
    while min_score + 1 < max_score:
        mid = (min_score+max_score)//2
        group = 0
        Totscore = 0
        for i in range(N):
            Totscore += scores[i]
            if Totscore >= mid:
                group += 1
                Totscore = 0
        
        if group < K:
            max_score = mid
        else:
            min_score = mid
    
    print(min_score)

binary_Search()