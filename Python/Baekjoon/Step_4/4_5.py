N = int(input())
M = list(map(int, input().split()))
avg = []
for i in M:
    avg.append(i/max(M)*100)
print(sum(avg)/N)

print(sum(M)*100/max(M)/N)