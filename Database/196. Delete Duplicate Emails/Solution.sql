# Write your MySQL query statement below

DELETE p
FROM Person p INNER JOIN Person p2
WHERE p.email = p2.email and p.id > p2.id;