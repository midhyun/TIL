croas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
line = input()
for croa in croas:
    line = line.replace(croa,'a')
print(len(line))
