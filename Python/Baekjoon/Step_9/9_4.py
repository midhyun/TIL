def star_square(num):
    if num == 1:
        return ['*']
    
    stars = star_square(num//3)
    lst = []

    for star in stars:
        lst.append(star*3)
    for star in stars:
        lst.append(star+' '*(num//3)+star)
    for star in stars:
        lst.append(star*3)
    
    return lst
num = int(input())
print('\n'.join(star_square(num)))
