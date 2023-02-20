clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

dic_c = {}
result = 1
for wear in clothes:
    dic_c[wear[1]] = dic_c.get(wear[1], 0) + 1

for k, v in dic_c.items():
    result *= (v+1)

result -= 1