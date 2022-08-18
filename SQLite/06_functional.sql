CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT * FROM users LIMIT 1;

SELECT
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;


SELECT 
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;

SELECT
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;

SELECT MOD(6, 2)    -- 나머지
FROM users
LIMIT 1;

SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.45)
FROM users
LIMIT 1;

SELECT SQRT(10)
FROM users
LIMIT 1;

SELECT POWER(age, 2), age
FROM users
LIMIT 5;