- 상품을 구매한 회원 비율 구하기
	- `USER_INFO` 테이블과 `ONLINE_SALE` 테이블에서 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력하는 SQL문을 작성해주세요. 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고, 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬해주세요.
```
SELECT YEAR, MONTH, COUNT(*) AS PUCHASED_USERS,
	ROUND((COUNT(*)/ (SELECT COUNT(*)
					FROM USER_INFO WHERE YEAR(JOINED) = 2021)), 1) AS PUCHASED_RATIO
FROM (
    SELECT DISTINCT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH, U.USER_ID
    FROM ONLINE_SALE S
    JOIN USER_INFO U ON S.USER_ID = U.USER_ID AND YEAR(JOINED) = 2021
) A
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH


WITH JOIN2021 AS (
    SELECT COUNT(DISTINCT USER_ID) AS NJ
    FROM USER_INFO WHERE YEAR(JOINED) = 2021)

SELECT YEAR, MONTH, COUNT(*) AS PUCHASED_USERS,
    ROUND((COUNT(*) / NJ), 1) AS PUCHASED_RATIO
FROM (
    SELECT DISTINCT YEAR(A.SALES_DATE) AS YEAR, MONTH(A.SALES_DATE) AS MONTH, B.USER_ID
    FROM ONLINE_SALE AS A
    JOIN USER_INFO AS B ON A.USER_ID = B.USER_ID AND YEAR(JOINED) = 2021
) AS C , JOIN2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;
```
- SELECT 절에서 서브쿼리의 사용은 지양하는 것이 좋다. 데이터의 양이 많아질수록 실행속도가 느려지므로 거의 사용하지 않는 명령어이다.
- FROM 절에서 서브쿼리의 사용은 **하나의 테이블 처럼** 사용 된다.
	- 따라서 열 이름과 테이블 명을 꼭 명시해주어야 한다. (ALIAS ERROR)

- **5월 식품들의 총매출 조회하기**
	- `FOOD_PRODUCT`와 `FOOD_ORDER` 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.
```
SELECT A.PRODUCT_ID, A.PRODUCT_NAME, B.TOTAL*PRICE AS TOTAL_SALES
FROM FOOD_PRODUCT AS A
JOIN (
    SELECT PRODUCT_ID, SUM(AMOUNT) AS TOTAL
    FROM FOOD_ORDER
    WHERE PRODUCE_DATE LIKE '2022-05%'
    GROUP BY PRODUCT_ID
) AS B ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID ASC;
```