with open('data/fruits.txt','r',encoding='utf-8') as f:
    print(len(list(f.read().split('\n'))))