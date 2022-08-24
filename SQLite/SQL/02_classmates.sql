-- classmates
-- name : TEXT
-- age : INT
-- address : TEXT

CREATE TABLE classmates (
    name TEXT,
    AGE INT,
    address TEXT
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER DEFAULT 1 CHECK (0 < age)
);

-- CREATE
-- INSERT INTO classmates VALUES ('홍길동', 23);

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');

SELECT rowid, * FROM classmates;

DROP TABLE classmates;