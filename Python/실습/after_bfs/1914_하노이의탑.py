def hanoi(start, end, n):
    if n == 1 :
        print(start, end)
        return

    hanoi(start, 6-start-end, n-1)
    print(start, end)
    hanoi(6-start-end, end, n-1)

n = int(input())
print(2**n -1)
if n < 20:
    hanoi(1, 3, n)