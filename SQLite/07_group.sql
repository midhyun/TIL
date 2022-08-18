SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name, age
FROM users
WHERE last_name = '곽';

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;

SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;

-- 실습 03

SELECT smoking, COUNT(smoking) FROM healthcare GROUP BY smoking;

SELECT is_drinking, COUNT(is_drinking) FROM healthcare GROUP BY is_drinking;

SELECT is_drinking, COUNT(is_drinking) 
FROM healthcare 
WHERE blood_pressure >= 200
GROUP BY is_drinking;

SELECT sido, count(sido) 
FROM healthcare 
GROUP BY sido 
HAVING COUNT(sido) >= 50000;

SELECT height, COUNT(height) CNT 
FROM healthcare 
GROUP BY height 
ORDER BY CNT 
DESC LIMIT 5;

SELECT weight, height, COUNT(weight) CNT 
FROM healthcare 
GROUP BY height, weight 
ORDER BY CNT DESC 
LIMIT 5;

SELECT is_drinking, AVG(waist), COUNT(waist) FROM healthcare GROUP BY is_drinking;

SELECT 
    gender,
    ROUND(AVG(va_left), 2) '평균 왼쪽 시력',
    ROUND(AVG(va_right),2) '평균 오른쪽 시력' 
FROM healthcare 
GROUP BY gender;

SELECT
    age,
    AVG(height) 평균_키,
    AVG(weight) 평균_몸무게
FROM healthcare
GROUP BY age
HAVING 평균_키 >= 160 AND 평균_몸무게 >= 60;

SELECT is_drinking, smoking, AVG(weight*10000/(height*height))
FROM healthcare
WHERE is_drinking != '' AND smoking != ''
GROUP BY is_drinking, smoking;

SELECT is_drinking, height, weight
FROM healthcare
LIMIT 5;