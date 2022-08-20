f_dict = {}

with open('data/fruits.txt','r',encoding='utf-8') as f:
    for i in list(f.read().split('\n')):
        f_dict[i] = f_dict.get(i,0)+1
with open('03.txt','w',encoding='utf-8') as f_2:
    for k, v in f_dict.items():
        f_2.write(k)
        f_2.write(f' {v}\n')
