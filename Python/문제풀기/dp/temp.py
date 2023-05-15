import sys
sys.stdin = open('temp.txt')
input = sys.stdin.readline

N = int(input())
W = int(input())
pos = [(1,1),(N,N)]
dp = [[-1] * (W+2) for _ in range(W+2)]
def search(row,col):
	if row > W or col > W:
		return 0
	if dp[row][col] != -1:
		return dp[row][col]
	next_pos = max(row,col) + 1
	nr = search(next_pos,col) + abs(pos[next_pos][0] - pos[row][0]) + abs(pos[next_pos][1] - pos[row][1])
	nc = search(row,next_pos) + abs(pos[next_pos][0] - pos[col][0]) + abs(pos[next_pos][1] - pos[col][1])
	dp[row][col] = min(nr,nc)
	return dp[row][col]

def route(row,col):
	if row > W or col > W:
		return
	next_pos = max(row,col)+1
	nr = abs(pos[next_pos][0]-pos[row][0]) + abs(pos[next_pos][1] - pos[row][1])
	nc = abs(pos[next_pos][0]-pos[col][0]) + abs(pos[next_pos][1] - pos[col][1])

	if dp[next_pos][col]+nr < dp[row][next_pos]+nc:
		print(1)
		route(next_pos,col)
	else:
		print(2)
		route(row,next_pos)
	return

def solution(N,W):
	print(search(0,1))
	route(0,1)

if __name__ == "__main__":
	for _ in range(W):
		pos.append(tuple(map(int,input().split())))
	solution(N,W)