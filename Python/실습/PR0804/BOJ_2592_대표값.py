import statistics
import sys
sys.stdin = open('2592.txt')
input = sys.stdin.readline
lst = []
for _ in range(10):
    lst.append(int(input()))

print(int(sum(lst)/len(lst)))
print(statistics.mode(lst))
