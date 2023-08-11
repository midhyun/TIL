import sys
sys.stdin = open('8983_사냥꾼.txt')
input = sys.stdin.readline

M, N, L = map(int, input().split())

shooting_pos = [*map(int, input().split())]
animal_pos = []
for _ in range(N):
    x, y = map(int, input().split())
    animal_pos.append((x, y))

shooting_pos.sort()

def binarySearch(s, e, animal):
    animal_x, animal_y = animal[0], animal[1]

    while s < e:
        mid = (s + e) // 2

        if shooting_pos[mid] < animal_x:
            s = mid + 1
        elif shooting_pos[mid] > animal_x:
            e = mid - 1
        else:
            s = mid
            break

    if abs(shooting_pos[s] - animal_x) + animal_y <= L:
        return True
    elif s + 1 < M and abs(shooting_pos[s+1] - animal_x) + animal_y <= L:
        return True
    elif s > 0 and abs(shooting_pos[s-1] - animal_x) + animal_y <= L:
        return True
    else:
        return False

answer = 0
for i in range(N):
    answer += binarySearch(0, M-1, animal_pos[i])

print(answer)