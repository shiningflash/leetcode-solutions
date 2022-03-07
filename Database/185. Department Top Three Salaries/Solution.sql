# Write your MySQL query statement below

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Department as d
JOIN Employee as e
WHERE
    e.departmentId = d.id and
    3 > (
        SELECT COUNT(DISTINCT(e2.salary))
        FROM Employee as e2
        WHERE
            e.departmentId = e2.departmentId and
            e2.salary > e.salary
    );