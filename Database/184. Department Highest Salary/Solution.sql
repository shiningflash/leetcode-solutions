# Write your MySQL query statement below

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Department d
JOIN Employee e
ON d.id = e.departmentId
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee e2
    WHERE e.departmentId = e2.departmentId
);

