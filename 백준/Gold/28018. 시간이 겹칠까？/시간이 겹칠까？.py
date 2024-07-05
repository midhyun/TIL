import sys
input = sys.stdin.readline

def sol():
    students = int(input())
    timeData = [0]*1000002
    
    for _ in range(students):
        start, end = map(int, input().split())
        timeData[start] += 1
        timeData[end+1] -= 1
        
    for t in range(1, 1000002):
        timeData[t] += timeData[t-1]
    
    questions, question = int(input()), [*map(int, input().split())]
    
    for q in question:
        print(timeData[q])

sol()