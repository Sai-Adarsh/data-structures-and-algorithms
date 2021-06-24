CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE IND INT;
    SET IND = N - 1;
    RETURN (
        # Write your MySQL query statement below.
        SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT IND, 1
        
    );
END