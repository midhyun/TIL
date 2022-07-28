remains = []
for i in range(10):
    remains.append(int(input()) % 42)
print(len(list(set(remains))))
