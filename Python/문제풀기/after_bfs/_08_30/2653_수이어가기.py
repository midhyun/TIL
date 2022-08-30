import sys
sys.stdin = open('2653_수이어가기.txt')
input = sys.stdin.readline

n = int(input())    # 첫 번째 수,
num_lst = []        # 첫 번째수보다 작은 임의의 수?

count = 0
answer = []
for second in range(1, n+1): 
    reserve_count = 0
    first = n
    third = n - second    
    reserve_answer = [first, second, third]
    while third >= 0:
        third = second - third
        second = first - second
        first = second + third
        reserve_count += 1
        reserve_answer.append(third)
    
    if count < reserve_count:
        count = reserve_count
        answer = reserve_answer

print(count+2)
for i in answer[:-1]:
    print(i,end= ' ')