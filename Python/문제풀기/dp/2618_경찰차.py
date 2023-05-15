import sys
sys.stdin = open('2618_경찰차.txt')
input = sys.stdin.readline

N = int(input())
W = int(input())
events = []
for _ in range(W):
    a, b = map(int, input().split())
    events.append((a, b))

for event in events:
    