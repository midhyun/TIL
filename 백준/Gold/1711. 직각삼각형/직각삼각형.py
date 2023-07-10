import sys
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    a, b = map(int, input().split())
    points.append((a, b))

result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            line1 = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            line2 = (points[j][0] - points[k][0])**2 + (points[j][1] - points[k][1])**2
            line3 = (points[k][0] - points[i][0])**2 + (points[k][1] - points[i][1])**2

            if 2*max(line1,line2,line3) == line1+line2+line3:
                result += 1

print(result)