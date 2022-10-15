n = int(input())

def promising(i):
    result = True
    for k in range(1, i):
        if col[k] == col[i] or abs(col[i] - col[k]) == i - k:
            result = False
            break
    return result

count = 0
def n_queens(i):
    global count
    if promising(i):
        if i == n:
            count += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1)
                
col = [0] * (n + 1)
n_queens(0)
print(count)