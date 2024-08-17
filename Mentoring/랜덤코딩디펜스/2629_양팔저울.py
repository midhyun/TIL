import sys
sys.stdin = open('2629_양팔저울.txt')
input = sys.stdin.readline

def solution(weights, bead):
    max_weights = sum(weights)
    dp = [False]*40001
    dp[0] = True

    for i in range(len(weights)):
        for j in range(max_weights,-1,-1):
            if dp[j]: dp[j+weights[i]] = True
        for j in range(max_weights+1):
            if dp[j]: dp[abs(j-weights[i])] = True
    
    if dp[bead]:
        return 'Y'
    else: return 'N'

weight_cnt, weights = int(input()), [*map(int, input().split())]
bead_cnt, beads = int(input()), [*map(int, input().split())]

for bead in beads:
    print(solution(weights, bead), end=' ')
print()