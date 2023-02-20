import sys
sys.stdin = open('14467.txt')
input = sys.stdin.readline

# 소의 위치 N번 관찰
# 각 관찰은 소의 번호, 소의 위치
# 소 10마리 있음
# 길의 왼쪽 0 , 오른쪽 1
# 소가 최소 몇번 길을 건넜는지 /
cow_dict = {}
N = int(input())
cnt = 0
for _ in range(N):
    cow_num, position = map(int, input().split())
    cow_dict[cow_num] = cow_dict.get(cow_num, position)
    if cow_dict[cow_num] != position:
        cnt += 1
        cow_dict[cow_num] = position
print(cnt)