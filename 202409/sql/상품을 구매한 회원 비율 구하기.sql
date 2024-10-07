SELECT 
    DATE_FORMAT(o.SALES_DATE, '%Y') AS YEAR, 
    DATE_FORMAT(o.SALES_DATE, '%m') AS MONTH,
    COUNT(DISTINCT o.USER_ID) AS PURCHASED_USERS,
    ROUND((COUNT(DISTINCT o.USER_ID) / (SELECT COUNT(USER_ID) FROM USER_INFO WHERE JOINED LIKE '2021%')) * 100, 2) AS PURCHASED_RATIO
FROM 
    USER_INFO u 
JOIN 
    ONLINE_SALE o ON u.USER_ID = o.USER_ID
WHERE 
    u.JOINED LIKE '2021%'
GROUP BY 
    YEAR, MONTH
ORDER BY 
    YEAR, MONTH;




상품을 구매한 회원 수: (이거는 21년에 구매하는게 아니라 21년에 이미 가입한 회원을 기준으로 하는 것이고, 그 조건은 where 절에서 이미 충족했으므로 따로 조건안걸어도 됨)
COUNT(DISTINCT o.USER_ID) as PURCHASED_USERS,
구매한회원의 비율 : 
ROUND((COUNT(DISTINCT o.USER_ID)/(SELECT COUNT(USER_ID) FROM USER_INFO WHERE JOINED LIKE '2021%'))*100,2) as PURCHASED_RATIO,