# Write your MySQL query statement below
SELECT W1.ID AS id
FROM Weather AS W1
INNER JOIN Weather AS W2
ON DATEDIFF(W1.RecordDate, W2.RecordDate) = 1
AND W1.Temperature > W2.Temperature