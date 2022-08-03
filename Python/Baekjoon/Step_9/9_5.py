def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, 1, 6-start-end)  # hanoi(n-1) n-1개를 옮긴다 1에서 6-s-e 로, 
    print(start, end)
    hanoi(n-1, 6-start-end, 3)


n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)