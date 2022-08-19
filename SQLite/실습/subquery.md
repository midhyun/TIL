```sql
-- 16 -1
SELECT Name									# 앨범 테이블에서 아티스트아이디로 그룹화해서
FROM artists								# 카운트의 값중 내림차순으로 첫번째 값이
WHERE ArtistId = (SELECT ArtistId 			# 가장 큰 카운트의 값
FROM albums 								# 카운트가 가장큰 행의 아티스트 아이디와
GROUP BY ArtistId 							# artists 테이블의 아티스트 아이디가 같을 때
ORDER BY COUNT(*) DESC LIMIT 1);			# 같은 행의 네임을 호출

-- 16 -2
SELECT Name									# 앨범 테이블에서 아티스트 아이디로 그룹화한
FROM artists								# 아티스트 아이디 별 앨범의 개수
WHERE ArtistId = (							# 로 호출한 출력값을 FROM으로 불러서
    SELECT ArtistId							# 그 중 ArtistID, MAX(CNT)로 출력
    FROM(									# 한 값을 또 FROM 으로 불러서
        SELECT ArtistId, MAX(CNT)			# ArtistID만 꺼냄, MAX(CNT)가 있으면 
        FROM (								# 아티스트 테이블의 아티스트 아이디와
            SELECT ArtistId,COUNT(*) 'CNT' 	# 일치 시킬 때 WHERE 에서 에러가 발생하므로
            FROM albums GROUP BY ArtistId	# 값의 개수를 일치시켜줌,
        )									# 아티스트 아이디에 해당하는 네임을 호출
    )
);
+-------------+
|    Name     |
+-------------+
| Iron Maiden |
+-------------+
-- 17 -1
SELECT Name									# 16번과 테이블, 컬럼 이름만 다름
FROM genres									# 내용은 같으며 MAX 대신 MIN 사용
WHERE GenreId = (SELECT GenreId
FROM tracks
GROUP BY GenreId
ORDER BY COUNT(*)
LIMIT 1);
-- 17 -2
SELECT Name
FROM genres
WHERE GenreId = (
    SELECT GenreId
    FROM(
        SELECT GenreId, MIN(CNT)
        FROM (
            SELECT GenreId,COUNT(*) 'CNT' 
            FROM tracks GROUP BY GenreId
        )
    )
);
+-------+
| Name  |
+-------+
| Opera |
+-------+
```

