-- 코드를 입력하세요
SELECT A.BOARD_ID, A.WRITER_ID, A.TITLE, A.PRICE, ( CASE A.STATUS 
                                                   WHEN 'DONE' THEN '거래완료'
                                                  WHEN 'SALE' THEN '판매중'
                                                  WHEN 'RESERVED' THEN '예약중' END) AS STATUS
FROM USED_GOODS_BOARD AS A
WHERE A.CREATED_DATE = '2022-10-05'
ORDER BY A.BOARD_ID DESC;