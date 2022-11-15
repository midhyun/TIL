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

