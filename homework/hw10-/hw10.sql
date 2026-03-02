.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height > sizes.min AND height <= sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT name FROM dogs, parents WHERE dogs.name = parents.child
    ORDER BY (SELECT height FROM dogs WHERE name = parents.parent) DESC;
-- 排序用 ORDER BY, DESC是降序

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  WITH siblings AS (
    SELECT a.child AS sib1, b.child AS sib2
    FROM parents AS a, parents AS b
    WHERE a.parent = b.parent AND a.child < b.child
  ),
  dog_sizes AS (
    SELECT d.name, s.size
    FROM dogs AS d, sizes AS s
    WHERE d.height > s.min AND d.height <= s.max
  )
  SELECT "The two siblings, " || s.sib1 || " plus " || s.sib2 || " have the same size: " || ds1.size
  FROM siblings AS s, dog_sizes AS ds1, dog_sizes AS ds2
  WHERE s.sib1 = ds1.name AND s.sib2 = ds2.name AND ds1.size = ds2.size;
-- 这部分是我想了很久没写明白的

-- The almighty midterm score of the SICP'25 students
CREATE TABLE midterm_almighty AS
  SELECT MAX(p1_wwpd) + MAX(p2_env) + MAX(p3_lists) + MAX(p4_functions) + MAX(p5_abstraction) + MAX(p6_tests) + MAX(p7_generators) + MAX(p8_bonus) AS total
  FROM midterm;


-- The total score distribution of SICP'25 midterm exam
CREATE TABLE midterm_distribution AS
  SELECT ROUND(FLOOR(total / 10) * 10, 1) AS bucket, COUNT(*) AS count FROM midterm
  GROUP BY bucket ORDER BY bucket DESC;