berry_list = []
with open('data/fruits.txt','r',encoding='utf-8') as f_r:
    f_list =list(map(str,f_r.read().split('\n')))
    for i in f_list:
        if i[-5:] == 'berry':
            if i not in berry_list:
                berry_list.append(i)

with open('02.txt','w',encoding='utf-8') as f_w:
    f_w.write(f'{len(berry_list)}\n')
    for i in berry_list:
        f_w.write(f'{i}\n')