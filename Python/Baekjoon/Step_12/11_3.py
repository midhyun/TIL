import sys
sys.stdin = open('11_3.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

poke_dict = {}
for i in range(1, N+1):
    j = input().strip()
    i = str(i)
    poke_dict[i] = poke_dict.get(i, j)
    poke_dict[j] = poke_dict.get(j, i)

for i in range(M):
    print(poke_dict[input().strip()])