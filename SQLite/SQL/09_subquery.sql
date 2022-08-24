-- 가장 나이가 작은 사람의 수
SELECT age, COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);

SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;

-- 평균보다 계좌 잔고가 높은 사람의 수
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- 유은정과 같은 지역에 사는 사람의 수
SELECT country, COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE last_name = '유' AND first_name = '은정');

SELECT
    (SELECT COUNT(*) FROM users) 총인원,
    (SELECT AVG(balance) FROM users) 평균연봉;

-- 이은정
SELECT
    country
FROM users
WHERE last_name = '이' AND first_name = '은정';
-- 동명이인, 도시가 두개
SELECT country, COUNT(*)
FROM users
WHERE country in (SELECT country FROM users WHERE last_name = '이' AND first_name = '은정')
GROUP BY country;


-- 특정 성씨별로 최소나이인 사람의 이름과 성
SELECT last_name 성, last_name || first_name 이름, age
FROM users
WHERE (last_name, age) IN (SELECT last_name, MIN(age)
FROM users
GROUP BY last_name)
ORDER BY age;


SELECT CustomerId,
    CASE
        WHEN Fax IS NULL THEN '무'
        ELSE '유'
    END AS 'FAX_유/무'
FROM customers 
ORDER BY CustomerId
LIMIT 5;
-- cast(BirthDate AS INTEGER) 월 일은 왜 날아가버리죠?
SELECT LastNAme, FirstName,
    (cast(strftime('%Y') AS INTEGER)-cast(strftime('%Y',BirthDate) AS INTEGER)+1) '나이'
FROM employees
ORDER BY EmployeeId;

-- SELECT
--     CASE
--         WHEN ArtistId IN (SELECT ArtistId FROM artists)
--         THEN (SELECT Name FROM artists WHERE artistId = '90')
--     END AS 'NAME',
-- COUNT(*) '앨범_수'
-- FROM albums
-- GROUP BY ArtistId
-- ORDER BY 앨범_수 DESC
-- LIMIT 1;

SELECT Name
FROM artists
WHERE ArtistId = (SELECT ArtistId FROM albums GROUP BY ArtistId HAVING COUNT(*) ORDER BY COUNT(*) DESC LIMIT 1)

SELECT GenreId
FROM tracks
GROUP BY GenreId
ORDER BY COUNT(*)
LIMIT 1;

SELECT Name
FROM genres
WHERE GenreId = (SELECT GenreId
FROM tracks
GROUP BY GenreId
ORDER BY COUNT(*)
LIMIT 1);
-- 16
SELECT Name
FROM artists
WHERE ArtistId = (
    SELECT ArtistId
    FROM(
        SELECT ArtistId, MAX(CNT)
        FROM (
            SELECT ArtistId,COUNT(*) 'CNT' 
            FROM albums GROUP BY ArtistId
            )
    )
);
-- 16
SELECT Name
FROM artists
WHERE ArtistId = (SELECT ArtistId 
FROM albums 
GROUP BY ArtistId 
ORDER BY COUNT(*) DESC LIMIT 1);
-- 17
SELECT Name
FROM genres
WHERE GenreId = (SELECT GenreId
FROM tracks
GROUP BY GenreId
ORDER BY COUNT(*)
LIMIT 1);
-- 17
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