-- INNER JOIN
-- A 와 B 테이블에서 값이 일치하는 것들만,
-- users 와 role 을 이너조인, user테이블 의 role_id 컬럼과
-- role테이블의 id 컬럼이 일치하는 것만 ! 
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   김철수   2        2   staff
-- 2   홍길동   2        2   staff
-- 3   관리자   1        1   admin

SELECT
    users.name,
    role.title
FROM users INNER JOIN role
    ON users.role_id = role.id;

SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

-- LEFT OUTER JOIN
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

SELECT *
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;

SELECT *
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;