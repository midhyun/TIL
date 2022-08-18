CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

.mode csv
.import users.csv users

SELECT * FROM users WHERE age >= 30;
SELECT last_name, first_name FROM users WHERE age >= 30;
SELECT last_name, first_name FROM users WHERE age >= 30 LIMIT 3;
SELECT last_name, first_name FROM users WHERE age >= 30 AND last_name = '김';

SELECT COUNT(*) FROM users WHERE age >= 30;
SELECT MIN(age) FROM users;
SELECT MIN(age) FROM users WHERE last_name = '이';
SELECT MIN(age), first_name FROM users WHERE last_name = '이';
SELECT first_name FROM users WHERE last_name = '이' AND age = 15;
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT MAX(balance), first_name FROM users;

-- 전화번호가 02- 로 시작하는 사람의 수
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

-- 오름차순 ASC(DEFAULT) 내림차순 DESC
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;


