import json
from pprint import pprint


def movie_info(movies, genres):
    result = []
    for m_dict in movies_list:
        gni = m_dict.get('genre_ids') # [18,80]
        lst = []
        for i in range(len(gni)):
            for j in genres:
                if j['id'] == gni[i]:
                    lst.append(j["name"])
        result.append({
            'genre_names': lst,
            'id' : m_dict.get('id'),
            'overview': m_dict.get('overview'),
            'title': m_dict.get('title'),
            'vote_average': m_dict.get('vote_average')
        })
    return result  

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
