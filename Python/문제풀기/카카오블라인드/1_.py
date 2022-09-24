from datetime import datetime
def solution(today, terms, privacies):
    today = [*map(int, today.split('.'))]
    today = datetime(today[0],today[1],today[2])
    terms_ = {}
    for i in terms:
        i = i.split(' ')
        terms_[i[0]] = int(i[1])
    answer = []
    for i in range(len(privacies)):
        privacy = privacies[i].split()
        date_get = [*map(int, privacy[0].split('.'))]
        expire = date_get[1] + terms_[privacy[1]]
        date_get[0] += expire//12
        date_get[1] = expire%12
        if date_get[1] == 0:
            date_get[1] = 12
            date_get[0] -= 1
        if date_get[2] == 1:
            date_get[2] = 28
            date_get[1] -= 1
            if date_get[1] == 0:
                date_get[1] = 12
                date_get[0] -= 1
        else: date_get[2] -= 1

        date_get = datetime(date_get[0],date_get[1],date_get[2])
        if date_get < today:
            answer.append(i+1)
    return answer