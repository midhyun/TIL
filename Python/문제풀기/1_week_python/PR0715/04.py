import json
from pprint import pprint


def movie_info(a): 
    result = {
        'genre_ids' : a.get('genre_ids'),
        'id' : a.get('id'),
        'overview' : a.get('overview'),
        'title' : a.get('title'),
        'vote_average' : a.get('vote_average')
    }
    return result ## 사용자함수 리턴을 쓰자.. 안쓰면 None

    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8') # 파이썬 객체 형식으로 한다 !
    movie = json.load(movie_json) # 로드!

    pprint(movie_info(movie))