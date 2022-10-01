import sys
sys.stdin = open('폰켓몬.txt')
input = sys.stdin.readline 
nums = [*map(int, input().split())]
def solution(nums):
    answer = 0
    n = len(nums)/2
    species = len(set(nums))
    if n >= species:
        answer = species
    else:
        answer = n
    return answer
print(solution(nums))