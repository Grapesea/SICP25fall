.read lab10_data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) == 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b 
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;
/*
时间戳是可以直接比较的，毕竟是字符串
别名设置的语法需要注意
*/

CREATE TABLE sevens AS
  SELECT students.seven FROM students,numbers WHERE students.number = 7 AND numbers."7" = 'True' AND students.time = numbers.time;
-- students.time = numbers.time 表示表的相同行，用来连接

CREATE TABLE avg_difference AS
  SELECT ROUND(AVG(ABS(number-smallest))) AS avg_diff FROM students;
-- 出来结果是1024.0

/*
CREATE TABLE correlation AS
  SELECT 
    SUM((ai_q1 - AVG(ai_q1)) * (midterm - AVG(midterm))) / 
      SQRT(SUM(POWER(ai_q1 - AVG(ai_q1), 2)) * SUM(POWER(midterm - AVG(midterm), 2)))
    AS ai_q1_correlation, 
    SUM((ai_q2 - AVG(ai_q2)) * (midterm - AVG(midterm))) / 
      SQRT(SUM(POWER(ai_q2 - AVG(ai_q2), 2)) * SUM(POWER(midterm - AVG(midterm), 2)))
    AS ai_q2_correlation
  FROM "lab0";
  */
-- SQL不允许嵌套aggregation，上面这个是错的

CREATE TABLE correlation AS
  SELECT 
    SUM((ai_q1 - avg_q1) * (midterm - avg_mid)) / 
      SQRT(SUM(POWER(ai_q1 - avg_q1, 2)) * SUM(POWER(midterm - avg_mid, 2)))
    AS ai_q1_correlation, 
    SUM((ai_q2 - avg_q2) * (midterm - avg_mid)) / 
      SQRT(SUM(POWER(ai_q2 - avg_q2, 2)) * SUM(POWER(midterm - avg_mid, 2)))
    AS ai_q2_correlation
  FROM "lab0", (SELECT AVG(ai_q1) AS avg_q1, AVG(ai_q2) AS avg_q2, AVG(midterm) AS avg_mid FROM "lab0") AS averages;