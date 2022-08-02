# 오르막길
# 수열의 수는 현재의 높이를 나타내며 수열의 차이로 오르막과 내리막을 구분함.
# 가장 큰 오르막길을 출력, 없을경우 0;
import sys
sys.stdin = open('input.txt')

N = int(input())
road = list(map(int, input().split()))
climb = 0
start = road[0]
ormac = []
for i in range(N):
    if start < road[i]:
        climb += road[i]-start
        start = road[i]

    else :
        ormac.append(climb)
        start = road[i]
        climb = 0
ormac.append(climb)
print(max(ormac))