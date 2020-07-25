## 입양 시각 구하기(2)

https://chanhuiseok.github.io/posts/db-6/



쿼리문에서 로컬 변수를 활용하는 문제



```mysql
SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23

```



```mysql
SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour

```

