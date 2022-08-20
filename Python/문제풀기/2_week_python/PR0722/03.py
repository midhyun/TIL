import requests
from pprint import pprint


def ranking():
    api_key = '7f612bfdbaa738cd44a88077eead2d22'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    result = []
    a = sorted(response.json()['results'], key =lambda x : x['vote_average'],reverse=True)
    for i in range(5):
        result.append(a[i])
    return result
    
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ranking())