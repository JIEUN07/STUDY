-- 1.
USE SAKILA;

-- 1. 1)
SELECT ACTOR_ID, FIRST_NAME, LAST_NAME
FROM ACTOR
ORDER BY FIRST_NAME;

-- 1. 2)
SELECT ACTOR_ID, FIRST_NAME, LAST_NAME
FROM ACTOR
WHERE LAST_NAME = 'WILLIAMS' OR 'DAVIS';

-- 1. 3)
SELECT RENTAL_ID, RENTAL_DATE
FROM RENTAL
WHERE DATE(RENTAL.RENTAL_DATE) = '2005-07-05';

-- 1. 4)
SELECT C.EMAIL, R.RETURN_DATE,
FROM CUSTOMER C
INNER JOIN RENTAL R
ON C.CUSTOMER_ID = R.CUSTOMER_ID
WHERE DATE(R.RENTAL_DATE) = '2005-06-14'
ORDER BY RETURN_DATE DESC;

-- 2. 1)
SELECT P.PAYMENT_ID, P.CUSTOMER_ID, P.PAYMENT_DATE, P.AMOUNT
FROM PAYMENT P
WHERE CUSTOMER_ID <> 5 AND (AMOUNT > 8 OR DATE(PAYMENT_DATE) = '2005-08-23');

-- 2. 2)
SELECT P.PAYMENT_ID, P.CUSTOMER_ID, P.PAYMENT_DATE, P.AMOUNT
FROM PAYMENT P
WHERE CUSTOMER_ID = 5 AND NOT (AMOUNT > 6 OR DATE(PAYMENT_DATE) = '2005-06-19');

-- 2. 3)
SELECT *
FROM PAYMENT
WHERE AMOUNT = 1.98 OR 7.98 OR 9.98;

-- 2. 4)
SELECT * FROM CUSTOMER
WHERE LAST_NAME LIKE '_AW%';

-- 3. 1)
USE BOOKSTORE;

SELECT * FROM BOOK
WHERE BOOKID = 1;

-- 3. 2)
SELECT * FROM BOOK
WHERE PRICE >=20000;

-- 3. 3)
SELECT C.CUSTID, C.NAME, O.CUSTID, O.BOOKID, O.SALEPRICE, SUM(SALEPRICE)
FROM CUSTOMER C
INNER JOIN ORDERS O
ON C.CUSTID = O.CUSTID
WHERE C.NAME='박지성';

-- 3. 4)
SELECT C.CUSTID, C.NAME, O.CUSTID, O.BOOKID, O.SALEPRICE, COUNT(NAME)
FROM CUSTOMER C
INNER JOIN ORDERS O
ON C.CUSTID = O.CUSTID
WHERE C.NAME='박지성';

-- 4. 1)
SELECT COUNT(BOOKNAME)
FROM BOOK;

-- 4. 2)
SELECT COUNT(PUBLISHER)
FROM BOOK;

-- 4. 3)
SELECT NAME, ADDRESS 
FROM CUSTOMER;

-- 4. 4)
SELECT ORDERID, ORDERDATE FROM ORDERS
WHERE DATE(ORDERS.ORDERDATE) BETWEEN '2014-07-04' AND '2014-07-07';

-- 4. 5)
SELECT ORDERID FROM ORDERS
WHERE DATE(ORDERS.ORDERDATE) NOT IN ('2014-07-04', '2014-07-07');

-- 4. 6)
SELECT ADDRESS, CUSTOMER.NAME
FROM CUSTOMER
WHERE NAME LIKE '김%';

-- 4. 7)
SELECT ADDRESS, CUSTOMER.NAME
FROM CUSTOMER
WHERE NAME LIKE '김%아';

