

SELECT
    CASE
        WHEN g.grade >= 8 THEN s.name      -- иначе вернётся NULL
    END                 AS name,
    g.grade             AS grade,
    s.marks             AS marks
FROM
    students AS s
JOIN
    grades   AS g
ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY
    grade DESC,         -- сначала по оценке
    name,               -- для 8–10 по имени (для <8 тут NULL)
    marks;              -- а для <8 — по баллам по возрастанию
