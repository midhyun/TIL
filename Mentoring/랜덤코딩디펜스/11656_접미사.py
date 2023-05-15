import sys
sys.stdin = open('11656_접미사.txt')
input = sys.stdin.readline

S = input().rstrip()
접미사 = []
for i in range(len(S)):
    접미사.append(S[i:])
접미사.sort()

for result in 접미사:
    print(result)