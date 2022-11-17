### 구글 Calendar API

- Event 추가하기

```
curl --request POST \
  'https://www.googleapis.com/calendar/v3/calendars/primary/events?sendUpdates=none&key=[YOUR_API_KEY]' \
  --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{"end":{"dateTime":"2022-11-16T13:00:00","timeZone":"Asia/Seoul"},"start":{"dateTime":"2022-11-16T13:00:00","timeZone":"Asia/Seoul"},"summary":"Calendar Test","location":"800 Howard St., San Francisco, CA 94103","description":"A chance to hear more about Googles developer products."}' \
  --compressed
```

```python
import json
import requests

url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events?sendUpdates=none&key=[YOUR_API_KEY]'
headers = {
    "Authorization": 'Bearer' + '[YOUR_ACCESS_TOKEN]',
    "Accept": 'application/json',
    "Content-Type": 'application/json',
}
data = {
    "end":{
        "dateTime":"2022-11-16T13:00:00",
        "timeZone":"Asia/Seoul"
    },
    "start":{
        "dateTime":"2022-11-16T13:00:00",
        "timeZone":"Asia/Seoul"
    },
    "summary":"Calendar Test",
    "location":"800 Howard St., San Francisco, CA 94103",
    "description":"A chance to hear more about Googles developer products."
}

response = requests.post(url, headers=headers, data=data)
if response.json().get('code') == 200:
    print('일정이 성공적으로 등록되었습니다.')
else:
    print('일정이 성공적으로 등록되지 못했습니다. 오류메시지 : ' + str(response.json()))
```

### 구글 토큰받기

```python
    google_base_url = "https://www.googleapis.com/auth"
    services = 
"google": {
        "base_url": "https://accounts.google.com/o/oauth2/v2/auth",
        "client_id": "925373116590-t4uf2ra8bkt25vegkjoskvi6054hd27u.apps.googleusercontent.com",  # 배포시 보안적용 해야함
        "redirect_uri": "http://localhost:8000/accounts/login/google/callback",
        "response_type": "code",
        "scope": f"{google_base_url}"
https://accounts.google.com/o/oauth2/v2/auth?client_id=503216611677-ah2v4o4cuqsustpbkvtot6ukdah6dhfp.apps.googleusercontent.com&redirect_uri=http://localhost:8000&response_type=code&scope=https://www.googleapis.com/calendar
"google": {
            "data": {
                "grant_type": "authorization_code",
                "redirect_uri": "http://localhost:8000/accounts/login/google/callback",
                "client_id": "925373116590-t4uf2ra8bkt25vegkjoskvi6054hd27u.apps.googleusercontent.com",  # 배포시 보안적용 해야함
                "client_secret": "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",  # 배포시 보안적용 해야함
                "state": request.GET.get("state"),
                "code": request.GET.get("code"),
            },
            "api": "https://oauth2.googleapis.com/token",
            "user_api": "https://www.googleapis.com/oauth2/v3/userinfo",
        }
    url = 'https://oauth2.googleapis.com/token'
    data = {
                "grant_type": "authorization_code",
                "redirect_uri": "http://localhost:8000/accounts/login/google/callback",
                "client_id": "925373116590-t4uf2ra8bkt25vegkjoskvi6054hd27u.apps.googleusercontent.com",  # 배포시 보안적용 해야함
                "client_secret": "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",  # 배포시 보안적용 해야함
                "state": request.GET.get("state"),
                "code": request.GET.get("code"),
            }
access_token = requests.post(
            services[service_name]["api"], data=services[service_name]["data"]
        ).json()["access_token"]
```

```python
{
    "web":{
    "client_id":"503216611677-ah2v4o4cuqsustpbkvtot6ukdah6dhfp.apps.googleusercontent.com",
    "project_id":"keen-button-368611",
    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    "token_uri":"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"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",
    "redirect_uris":["http://localhost:8000"],
    "javascript_origins":["http://localhost:8000"]
}}
```

```
{% if review.image %}
 <a><img></a>
{% else %}
 <a><img dummy></a>
{% endif %}


 
```

