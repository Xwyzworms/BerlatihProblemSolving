SELECT months * salary as earnings, count(*) FROM  Employee
GROUP BY earnings 
ORDER BY Earnings DESC
LIMIT 1;