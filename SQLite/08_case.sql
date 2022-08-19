SELECT id, gender
FROM users
LIMIT 5;

SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남성'
        WHEN gender = 2 THEN '여성'
        ELSE '무응답'
    END AS 성별
FROM healthcare
LIMIT 5;

SELECT DISTINCT smoking
FROM healthcare;

SELECT
    id,
    smoking
    CASE
        WHEN smoking = 1 THEN '비흡연'
        WHEN smoking = 2 THEN '흡연충'
        WHEN smoking = 3 THEN '술담충'
        ELSE '무응답'
    END AS 담배
FROM healthcare
LIMIT 50;

SELECT
    first_name,
    last_name,
    age,
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 40 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년'
    END
FROM users
LIMIT 10;
    