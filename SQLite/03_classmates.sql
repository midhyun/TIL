CREATE TABLE classmates (
    name TEXT NOT NULL,
    age TEXT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

SELECT * FROM classmates;

SELECT rowid, name FROM classmates;
-- 1|홍길동
-- 2|김철수
-- 3|이호영
-- 4|박민희
-- 5|최혜영

SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   30   서울
-- 2      김철수   30   제주
-- 3      이호영   26   인천
-- 4      박민희   29   대구
-- 5      최혜영   28   전주
SELECT rowid, name FROM classmates LIMIT 2;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT * FROM classmates WHERE address = '서울';

SELECT name FROM classmates WHERE age >= 30;

SELECT DISTINCT age FROM classmates;

SELECT DISTINCT address FROM classmates;

DELETE FROM classmates WHERE rowid = 5;

INSERT INTO classmates VALUES ('김현중', 28, '고양');
SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   30   제주
3      이호영   26   인천
4      박민희   29   대구
5      최혜영   28   전주
6      김현중   28   고양

UPDATE classmates SET name = '홍길동', address='제주도' WHERE rowid = 5;
SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   30   제주
3      이호영   26   인천
4      박민희   29   대구
5      홍길동   28   제주도
6      김현중   28   고양

SELECT rowid, name FROM classmates LIMIT 100;

