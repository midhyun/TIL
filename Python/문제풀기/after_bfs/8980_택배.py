import sys
sys.stdin = open('8980_택배.txt')
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

boxes = [list(map(int, input().split())) for _ in range(m)]
boxes.sort(key=lambda x:x[1]) # 마을 도착 시간이 빠른 것 순으로 정렬

count = 0
remains = [c]*(n+1) # 마을 당 수용가능한 박스 수

for i in range(m):
    temp = c # c개를 옮길 수 있다고 가정
    for j in range(boxes[i][0], boxes[i][1]):
        temp = min(temp, remains[j])
    temp = min(temp, boxes[i][2])
    for k in range(boxes[i][0], boxes[i][1]):
        remains[k] -= temp
    count += temp

print(count)