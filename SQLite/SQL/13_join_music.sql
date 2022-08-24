-- 1
SELECT * FROM playlist_track AS A ORDER BY PlaylistId DESC LIMIT 5;
-- 3
SELECT A.PlaylistId, B.Name
FROM playlist_track A
    JOIN tracks B
        ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId
LIMIT 10;

--4
SELECT A.playlistId, B.Name
FROM playlist_track A
    JOIN tracks B
        ON A.TrackId = B.TrackId
WHERE A.playlistId = 10
ORDER BY B.Name
LIMIT 5;

-- 5
SELECT COUNT(*)
FROM tracks A
    INNER JOIN artists B 
    ON A.Composer = B.Name;

-- 6
SELECT COUNT(*)
FROM tracks A 
    LEFT JOIN artists B 
    ON A.Composer = B.Name;

-- 7
-- INNER JOIN 의 경우 동일한 값이 있는 경우에만 출력하는 반면
-- LEFT (OUTER) JOIN 의 경우 B에 값이 없더라도 
-- A에 값 이있으면 NULL로 출력하기 때문

-- 8
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;

-- 9
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;

-- 10
SELECT A.InvoiceLineId, A.InvoiceID
FROM invoice_items A
    LEFT JOIN invoices B 
    ON A.InvoiceId = B.invoiceId
ORDER BY A.InvoiceId DESC
LIMIT 5;

-- 11
SELECT A.InvoiceId, B.CustomerId
FROM invoices A
    LEFT JOIN customers B 
    ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;

-- 12
SELECT A.InvoiceLineId, A.InvoiceId, B.CustomerId
FROM invoice_items A
    LEFT JOIN invoices B 
    ON A.InvoiceId = B.invoiceId
ORDER BY A.InvoiceId
LIMIT 5;

-- 13
SELECT B.CustomerId, COUNT(*)
FROM invoice_items A
    LEFT JOIN invoices B 
    ON A.InvoiceId = B.invoiceId
GROUP BY B.CustomerId
ORDER BY B.CustomerId
LIMIT 5;

SELECT Country, COUNT(*)
FROM customers
GROUP BY Country
ORDER BY COUNT(*) DESC
LIMIT 5;

SELECT Country, COUNT(*) CNT
FROM invoices AS A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
WHERE strftime('%Y', InvoiceDate) = '2010' 
GROUP BY B.Country
ORDER BY CNT DESC
LIMIT 10;

-- extra
-- ArtistId, Name, 각 Artist가 낸 tracks의 수 출력, 트랙 수 기준 내림차순, 10개

SELECT artists.artistId, artists.Name, COUNT(*) CNT
FROM tracks 
    INNER JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    INNER JOIN artists
    ON albums.artistId = artists.artistId
GROUP BY artists.artistId
ORDER BY CNT DESC
LIMIT 10;