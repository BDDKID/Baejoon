-- 코드를 입력하세요
SELECT  C.car_id
FROM CAR_RENTAL_COMPANY_CAR C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
WHERE CAR_TYPE = '세단' AND START_DATE LIKE '2022-10%'
GROUP BY C.car_id
ORDER BY C.car_id DESC
