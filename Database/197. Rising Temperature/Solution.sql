# Write your MySQL query statement below

# Approach 1

SELECT w.id
FROM
    Weather w
    INNER JOIN Weather w2
WHERE
    TO_DAYS(w.recordDate) - TO_DAYS(w2.recordDate) = 1
    AND w.temperature > w2.temperature;

# Approach 2

SELECT w.id
FROM
    Weather w
    INNER JOIN Weather w2
WHERE
    Datediff(w.recordDate, w2.recordDate) = 1
    AND w.temperature > w2.temperature;