import sys
sys.stdin = open('28018_시간이겹칠까.txt')
input = sys.stdin.readline

def solution():
    students = int(input())
    times = []
    endStack = []
    for _ in range(students):
        startTime, endTime = map(int, input().split())
        times.append(startTime)
        endStack.append(endTime)
    times.append(1000003)
    times.sort()
    endStack.sort(reverse=True)
    questions = int(input())
    question = [*map(int, input().split())]

    sits = [0]*1000003
    cur = 0
    timeIdx = 1

    for start in times:
        while timeIdx < start:
            sits[timeIdx] = cur
            while endStack:
                if endStack[-1] == timeIdx:
                    endStack.pop()
                    cur -= 1
                    continue
                else:
                    break
            timeIdx += 1
        
        cur += 1

    for questionTime in question:
        print(sits[questionTime])

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

solution()