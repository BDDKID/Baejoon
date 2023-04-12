# desc USER_INFO / pk : user_id
# desc ONLINE_SALE / pk : online_sale_id, fk : user_id
# USER_INFO 테이블과 ONLINE_SALE 테이블에서 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 
# 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력 
# 
# 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고, 
# 년을 기준으로 오름차순 월을 기준으로 오름차순
SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MONTH, 
        COUNT(DISTINCT U.USER_ID) AS PUCHASED_USERS,
        ROUND(COUNT(DISTINCT U.USER_ID)/(SELECT COUNT(*) 
                                         FROM USER_INFO
                                         WHERE YEAR(JOINED) = 2021),1) AS PUCHASED_RATIO
FROM USER_INFO U JOIN ONLINE_SALE S ON U.USER_ID = S.USER_ID
WHERE YEAR(U.JOINED) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH

