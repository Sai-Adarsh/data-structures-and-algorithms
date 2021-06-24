# Write your MySQL query statement below
SELECT SCORE, DENSE_RANK() OVER(ORDER BY score DESC) AS "Rank" FROM SCORES