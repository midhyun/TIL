from collections import defaultdict
import sys
sys.stdin = open('2143_두배열의합.txt')
input = sys.stdin.readline

def solution():
    T = int(input())
    n, A = int(input()), [*map(int, input().split())]
    m, B = int(input()), [*map(int, input().split())]
    answer = 0

    sum_A, sum_B = [0], [0]
    partialSumA, partialSumB = defaultdict(int), defaultdict(int)

    for i in range(n):
        sum_A.append(A[i] + sum_A[i])
        for j in range(i+1):
            partialSumA[sum_A[i+1] - sum_A[j]] += 1
    
    for i in range(m):
        sum_B.append(B[i] + sum_B[i])
        for j in range(i+1):
            partialSumB[sum_B[i+1] - sum_B[j]] += 1
    
    for key in partialSumA.keys():
        if T - key in partialSumB:
            answer += partialSumA[key] * partialSumB[T - key]

    print(answer)
    return

solution()