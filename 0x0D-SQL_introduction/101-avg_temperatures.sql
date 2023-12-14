-- Import in hbtn_0c_0 database this table dump - temperatures.sql
-- Calculating the average temperature (Fahrenheit) by city and ordering by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
