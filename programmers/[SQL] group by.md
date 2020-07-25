# GROUP BY  [column]



- `GROUP BY`는 `DISTINCT`와 달리 집계함수를 사용할 수 있다.

  - `DISTINCT`는 범주를 확인할 때 사용

    ```mysql
    # 1
    SELECT DISTINCT NAME FROM ANIMAL_INS;
    ```

    ```mysql
    # 2
    SELECT DISTINCT NAME FROM ANIMAL_INS WHERE [condition];
    ```

    ```mysql
    # 3
    SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS;
    ```

  - `GROUP BY`

    ```mysql
    # 위의 1번과 같은 결과
    SELECT NAME FROM ANIMAL_INS GROUP BY NAME;
    ```

  - 조건 처리 후 그룹화

    ```mysql
    SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼;
    ```

  - 그룹화 후 조건 처리

    ```mysql
    SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼 HAVING 조건식;
    ```

    

- NULL 주의

```mysql
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME;
```

```mysql
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT >= 2 ORDER BY NAME;
```

```mysql
# WRONG
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(*) >= 2 ORDER BY NAME;
```

```mysql
# WRONG
SELECT NAME, COUNT(*) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT >= 2 ORDER BY NAME;
```

