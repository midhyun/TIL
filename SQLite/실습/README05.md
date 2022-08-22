### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT * FROM playlist_track AS A ORDER BY PlaylistId DESC LIMIT 5;
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT * FROM tracks AS B ORDER BY TrackId LIMIT 5;
TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer                                                      Milliseconds  Bytes     UnitPrice
-------  ---------------------------------------  -------  -----------  -------  ------------------------------------------------------------  ------------  --------  ---------
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99

2        Balls to the Wall                        2        2            1                                                                      342562        5510424   0.99

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99
                                                                                 W. Hoffman

5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99
```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT A.PlaylistId, B.Name
FROM playlist_track A
    JOIN tracks B
        ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC
LIMIT 10;
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.playlistId, B.Name
FROM playlist_track A
    JOIN tracks B
        ON A.TrackId = B.TrackId
WHERE A.playlistId = 10
ORDER BY B.Name DESC
LIMIT 5;
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.

```sql
SELECT COUNT(*)
FROM tracks A
    INNER JOIN artists B 
    ON A.Composer = B.Name;
COUNT(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.

```sql
SELECT COUNT(*)
FROM tracks A 
    LEFT JOIN artists B 
    ON A.Composer = B.Name;
COUNT(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
-- INNER JOIN 의 경우 동일한 값이 있는 경우에만 출력하는 반면
-- LEFT (OUTER) JOIN 의 경우 B에 값이 없더라도 
-- A에 값 이있으면 NULL로 출력하기 때문
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.InvoiceLineId, A.InvoiceID
FROM invoice_items A
    INNER JOIN invoices B 
    ON A.InvoiceId = B.invoiceId
ORDER BY A.InvoiceId DESC
LIMIT 5;
+---------------+-----------+
| InvoiceLineId | InvoiceId |
+---------------+-----------+
| 2240          | 412       |
| 2226          | 411       |
| 2227          | 411       |
| 2228          | 411       |
| 2229          | 411       |
+---------------+-----------+
```


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```SQL
SELECT A.InvoiceId, B.CustomerId
FROM invoice_items A
    LEFT JOIN invoices B 
    ON A.InvoiceId = B.invoiceId
ORDER BY A.InvoiceId DESC
LIMIT 5;
InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```SQL
SELECT A.InvoiceLineId, B.InvoiceId, C.CustomerId
FROM invoice_items A
    INNER JOIN invoices B 
    ON A.InvoiceId = B.invoiceId
    INNER JOIN customers C
    ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT B.CustomerId, COUNT(*)
FROM invoice_items A
    INNER JOIN invoices B
    ON A.InvoiceId = B.InvoiceId
GROUP BY B.CustomerId
ORDER BY B.CustomerId
LIMIT 5;
CustomerId  COUNT(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```

### 14. 각 나라Country 별 고객의 수를 내림차순으로 출력하세요.

> LIMIT 5

```sql
SELECT Country, COUNT(*)
FROM customers
GROUP BY Country
ORDER BY COUNT(*) DESC
LIMIT 5;
+---------+----------+
| Country | COUNT(*) |
+---------+----------+
| USA     | 13       |
| Canada  | 8        |
| France  | 5        |
| Brazil  | 5        |
| Germany | 4        |
+---------+----------+
```



### 15.  각 나라County 별 주문 건수, 주문한 물건 개수를 건수 기준으로 내림차순으로 출력하세요. 

> LIMIT 10

```sql
SELECT Country, COUNT(*) CNT, items
FROM invoices AS A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
    INNER JOIN invoice_items C
    ON A.InvoiceId = C.InvoiceId
    INNER JOIN (SELECT BillingCountry, COUNT(*) items
FROM invoices
GROUP BY BillingCountry) D
	ON B.Country = D.BillingCountry
GROUP BY B.Country
ORDER BY CNT DESC
LIMIT 10;

+----------------+-----+-------+
|    Country     | CNT | items |
+----------------+-----+-------+
| USA            | 494 | 91    |
| Canada         | 304 | 56    |
| France         | 190 | 35    |
| Brazil         | 190 | 35    |
| Germany        | 152 | 28    |
| United Kingdom | 114 | 21    |
| Portugal       | 76  | 14    |
| Czech Republic | 76  | 14    |
| India          | 74  | 13    |
| Sweden         | 38  | 7     |
+----------------+-----+-------+
```

### 16. 2010년 에 주문한 각 나라Country 별 주문한 물건의 개수를 개수를 기준으로 내림차순으로 출력하세요.

> LIMIT 10

```sql
-- 1 주문 물건 개수
SELECT Country, COUNT(C.InvoiceLineId) CNT, COUNT(A.InvoiceId) Ord, COUNT(*)
FROM invoices AS A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
    INNER JOIN Invoice_items C
    ON A.InvoiceId = C.InvoiceId
WHERE strftime('%Y', A.InvoiceDate) = '2010' 
GROUP BY B.Country
ORDER BY CNT DESC
LIMIT 10;
-- 2 주문 건수
SELECT Country, COUNT(*) CNT
FROM invoices AS A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
WHERE strftime('%Y', InvoiceDate) = '2010'
GROUP BY B.Country
ORDER BY CNT DESC
LIMIT 10;

-- 3 둘다 함께 출력
SELECT Country, COUNT(*) CNT, items
FROM invoices AS A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
    INNER JOIN (SELECT BillingCountry, Count(*) items
FROM invoice_items A
INNER JOIN invoices B
ON A.InvoiceId = B.InvoiceId
GROUP BY B.BillingCountry) C
	ON B.Country = C.BillingCountry
WHERE strftime('%Y', InvoiceDate) = '2010'
GROUP BY B.Country
ORDER BY CNT DESC
LIMIT 10;
-- 3-2 서브쿼리
SELECT BillingCountry, Count(*)
FROM invoice_items A
INNER JOIN invoices B
ON A.InvoiceId = B.InvoiceId
GROUP BY B.BillingCountry;

+----------------+-----+-------+
|    Country     | CNT | items |
+----------------+-----+-------+
| USA            | 18  | 494   |
| Canada         | 12  | 304   |
| France         | 8   | 190   |
| Brazil         | 8   | 190   |
| United Kingdom | 5   | 114   |
| Germany        | 4   | 152   |
| Portugal       | 3   | 76    |
| Italy          | 3   | 38    |
| India          | 3   | 74    |
| Hungary        | 3   | 38    |
+----------------+-----+-------+
```

### 17.ArtistId, Name, 각 Artist가 낸 tracks의 수 출력, 트랙 수 기준 내림차순, 10개

```sql
SELECT artists.artistId, artists.Name, COUNT(*) CNT
FROM tracks 
    INNER JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    INNER JOIN artists
    ON albums.artistId = artists.artistId
GROUP BY artists.artistId
ORDER BY CNT DESC
LIMIT 10;
+----------+-----------------+-----+
| ArtistId |      Name       | CNT |
+----------+-----------------+-----+
| 90       | Iron Maiden     | 213 |
| 150      | U2              | 135 |
| 22       | Led Zeppelin    | 114 |
| 50       | Metallica       | 112 |
| 58       | Deep Purple     | 92  |
| 149      | Lost            | 92  |
| 118      | Pearl Jam       | 67  |
| 100      | Lenny Kravitz   | 57  |
| 21       | Various Artists | 56  |
| 156      | The Office      | 53  |
+----------+-----------------+-----+
```
