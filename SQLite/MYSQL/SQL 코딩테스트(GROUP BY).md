- **가격대 별 상품 개수 구하기**
	- `PRODUCT`테이블에서 만원 단위의 가겨대 별로 상품 개수를 출력하는 SQL문을 작성해 주세요. 이때 컬럼명은 각각 PRICE_GROUP, PRODUCTTS로 지정해주시고 가격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시해주세요. 결과는 가격대를 기준으로 오름차순 정렬해주세요.
```MYSQL
SELECT TRUNCATE(PRICE,-4) AS PRICE_GROUP, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP ASC;
```

- TRUNCATE(숫자, 자릿수): 자릿수만큼의 숫자를 버린다.
- EX) TRUNCATE(1234.567, 1) = 1234.5

- **년, 월, 성별 별 상품 구매 회원 수 구하기**
```MYSQL
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT A.USER_ID) AS USERS
FROM ONLINE_SALE AS A
JOIN USER_INFO AS B ON A.USER_ID = B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR(SALES_DATE), MONTH(SALES_dATE), GENDER
ORDER BY YEAR(SALES_DATE), MONTH(SALES_dATE), GENDER;
```

- **자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기**
```MYSQL
SELECT CAR_TYPE, COUNT(CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC;
```
- 옵션의 종류에 '시트' 가 포함된 것들중 하나라도 나오면 되므로 위같은 쿼리문으로도 가능했음
- 이전에는 LIKE '조건1' OR LIKE '조건2' 와 같이 작성함

- **성분으로 구분한 아이스크림 총 주문량**
	- 상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을 총주문량이 작은 순서대로 조회하는 SQL문을 작성 해주세요. 이때 총 주문량을 나타내는 칼럼명은 TOTAL_ORDER로 지정해주세요.
```MYSQL
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO AS A
JOIN FIRST_HALF AS B ON A.FLAVOR = B.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
```

- 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
	- `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: `AVAILABILITY`)을 추가하여 자동차 ID와 `AVAILABILITY` 리스트를 출력하는 SQL문을 작성해주세요. 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.
```MYSQL
SELECT CAR_ID, MAX(
    CASE
        WHEN '2022-10-16' BETWEEN DATE_FORMAT(START_DATE, '%Y-%m-%d') AND DATE_FORMAT(END_DATE, '%Y-%m-%d')
        THEN '대여중'
        ELSE '대여 가능'
    END
    ) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
```
