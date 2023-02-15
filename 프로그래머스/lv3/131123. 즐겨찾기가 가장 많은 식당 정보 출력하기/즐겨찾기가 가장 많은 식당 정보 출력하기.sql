-- 코드를 입력하세요
SELECT B.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM REST_INFO AS A,
    (SELECT FOOD_TYPE, MAX(FAVORITES) AS MFAVOR
    FROM REST_INFO
    GROUP BY FOOD_TYPE) AS B
WHERE A.FAVORITES = B.MFAVOR AND A.FOOD_TYPE = B.FOOD_TYPE
ORDER BY FOOD_TYPE DESC;