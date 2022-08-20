import requests
from pprint import pprint
import os
from dotenv import load_dotenv

def credits(title):
    try:

        load_dotenv()
        api_key = os.getenv('api_key')
        URL = 'https://api.themoviedb.org/3'
        path_1 = '/search/movie'
        param_1 = {
            'api_key' : api_key,
            'language' : 'ko_KR',
            'query' : title
        }
        response_search = requests.get(URL + path_1, params = param_1)
        movie_id = response_search.json()['results'][0].get('id')

        path_2 = f'/movie/{movie_id}/credits'
        param_2 = {
            'api_key' : api_key,
            'language' : 'ko_KR'
        }
        lst_crew = []
        lst_cast = []
        response_search = requests.get(URL + path_2, params=param_2).json()
        crew = response_search.get('crew') # list
        cast = response_search.get('cast') # list

        for i in cast:
            if int(i['cast_id']) < 10 :
                lst_cast.append(i['name'])
        for j in crew: # i = {} dict
            if j['department'] == 'Directing' :
                lst_crew.append(i['name'])


        result = {
            'cast' : lst_cast,
            'crew' : lst_crew
        }
        return result
    except:
        None
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
