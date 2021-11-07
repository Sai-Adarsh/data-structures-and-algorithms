# Write your MySQL query statement below
SELECT DISTINCT(L1.num) AS ConsecutiveNums 
FROM Logs L1, Logs L2, Logs L3
WHERE L1.id - L2.id = 1 AND L2.id - L3.id = 1 
AND (L1.num = L2.num AND L2.num = L3.num)