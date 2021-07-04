SELECT DISTINCT(A.id)
FROM WEATHER A, WEATHER B
WHERE A.Temperature > B.Temperature
AND DATEDIFF(A.recordDate, B.recordDate) = 1