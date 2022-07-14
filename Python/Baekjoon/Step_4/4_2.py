Nat = []
Mx = 0
cnt = 0
for i in range(9):
    Nat.append(int(input()))
    if Nat[i] >= Mx:
        Mx = Nat[i]
        cnt = i+1
print(Mx)
print(cnt)