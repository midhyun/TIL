genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]

dic = {}
answer = []
for i, (genre, play) in enumerate(zip(genres, plays)):
    try:
        dic[genre] = [dic[genre][0] + play, dic[genre][1] + [(play, i)]]
    except:
        dic[genre] = [play, [(play, i)]]

for _, idxs in sorted(dic.items(), key=lambda x: -x[1][0]):
    for idx in sorted(idxs[1], key=lambda x: -x[0])[:2]:
        answer.append(idx[1])

print(dic)
print(answer)