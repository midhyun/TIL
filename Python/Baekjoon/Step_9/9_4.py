def star_stamp(num):
    if num == 1:
        return['*']

    stars = star_stamp(num//3)
    lst = []
    for star in stars:
        lst.append(star*3)
    for star in stars:
        lst.append(star+' '*(num//3)+star)
    for star in stars:
        lst.append(star*3)
    return lst

num = int(input())
print('\n'.join(star_stamp(num)))
print(star_stamp(num))